#!/usr/bin/env python3
"""Extrai DFP/ITR da ENGIE Brasil Energia a partir dos dados abertos da CVM.

A fonte oficial é https://dados.cvm.gov.br/. Os valores não são inventados:
eles são lidos diretamente dos CSVs disponibilizados pela CVM.
"""

from __future__ import annotations

import io
import sys
import time
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests
from openpyxl.styles import Alignment, Font

# =========================== CONFIGURAÇÃO ===========================
CNPJ_ALVO = "02.474.103/0001-19"
NOME_SAIDA = "demonstracoes_engie.xlsx"
ANOS_ANUAIS = 5
ANO_INICIAL_ITR = datetime.now().year  # exercício corrente por padrão
MAX_TENTATIVAS = 4
TIMEOUT_SEGUNDOS = 90
PASTA_CACHE = Path(".cache_cvm")

# A CVM usa estes sufixos nos nomes dos arquivos dentro dos ZIPs.
DEMOS = {
    "BPA": "BPA",
    "BPP": "BPP",
    "DRE": "DRE",
    "DFC_MD": "DFC_MD",
    "DFC_MI": "DFC_MI",
    "DMPL": "DMPL",
    "DVA": "DVA",
    "DRA": "DRA",
}

URL_DFP = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{ano}.zip"
URL_ITR = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_{ano}.zip"

COLUNAS_BASE = [
    "CNPJ_CIA", "DT_REFER", "VERSAO", "DENOM_CIA", "CD_CVM",
    "GRUPO_DFP", "MOEDA", "ESCALA_MOEDA", "ORDEM_EXERC",
    "DT_FIM_EXERC", "CD_CONTA", "DS_CONTA", "VL_CONTA", "ST_CONTA_FIXA",
]


def aviso(msg: str) -> None:
    print(f"[AVISO] {msg}", file=sys.stderr)


def baixar_zip(url: str, destino: Path) -> bytes | None:
    """Baixa um ZIP com retentativas e cache local."""
    if destino.exists() and destino.stat().st_size > 0:
        return destino.read_bytes()

    headers = {"User-Agent": "Mozilla/5.0 (compatible; CVM-data-extractor/1.0)"}
    ultima_excecao: Exception | None = None
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            resposta = requests.get(url, headers=headers, timeout=TIMEOUT_SEGUNDOS)
            if resposta.status_code == 404:
                aviso(f"Arquivo ainda não disponível: {url}")
                return None
            resposta.raise_for_status()
            if not resposta.content.startswith(b"PK"):
                raise ValueError("a resposta não parece ser um arquivo ZIP")
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_bytes(resposta.content)
            return resposta.content
        except (requests.RequestException, ValueError, OSError) as exc:
            ultima_excecao = exc
            if tentativa < MAX_TENTATIVAS:
                espera = 2 ** (tentativa - 1)
                print(f"Tentativa {tentativa} falhou; nova tentativa em {espera}s...")
                time.sleep(espera)
    aviso(f"Não foi possível baixar {url}: {ultima_excecao}")
    return None


def ler_csv_do_zip(zbytes: bytes, nome: str) -> pd.DataFrame | None:
    """Lê CSV da CVM com encoding e separador oficiais."""
    with zipfile.ZipFile(io.BytesIO(zbytes)) as zf:
        candidatos = [n for n in zf.namelist() if n.lower().endswith(".csv")]
        exato = next((n for n in candidatos if n.lower() == nome.lower()), None)
        if exato is None:
            aviso(f"CSV ausente no ZIP: {nome}")
            return None
        with zf.open(exato) as arquivo:
            return pd.read_csv(
                arquivo,
                sep=";",
                encoding="latin-1",
                dtype={"CNPJ_CIA": "string", "CD_CVM": "string", "CD_CONTA": "string"},
                low_memory=False,
            )


def normalizar(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza datas, versão e valores monetários."""
    if df is None or df.empty:
        return pd.DataFrame(columns=COLUNAS_BASE)

    for col in COLUNAS_BASE:
        if col not in df.columns:
            df[col] = pd.NA

    df = df[COLUNAS_BASE].copy()
    df["CNPJ_CIA"] = df["CNPJ_CIA"].astype("string").str.strip()
    df["CD_CVM"] = df["CD_CVM"].astype("string").str.strip()
    df["CD_CONTA"] = df["CD_CONTA"].astype("string").str.strip()
    df["DS_CONTA"] = df["DS_CONTA"].astype("string").str.strip()
    df["DT_REFER"] = pd.to_datetime(df["DT_REFER"], errors="coerce")
    df["DT_FIM_EXERC"] = pd.to_datetime(df["DT_FIM_EXERC"], errors="coerce")
    df["VERSAO"] = pd.to_numeric(df["VERSAO"], errors="coerce").fillna(1).astype(int)

    # A CVM normalmente entrega ponto decimal; o fallback trata eventuais vírgulas.
    bruto = df["VL_CONTA"].astype("string").str.strip()
    bruto = bruto.str.replace(".", "", regex=False).where(
        ~bruto.str.contains(r",\d+$", na=False),
        bruto.str.replace(".", "", regex=False).str.replace(",", ".", regex=False),
    )
    # Para o formato usual 12345.670000000, preserve o ponto decimal.
    usual = df["VL_CONTA"].astype("string").str.replace(",", ".", regex=False)
    df["VL_CONTA"] = pd.to_numeric(usual, errors="coerce")
    return df


def localizar_codigo_cvm(dfs: Iterable[pd.DataFrame]) -> str | None:
    """Confirma CD_CVM pelo CNPJ, sem fixar o código no código-fonte."""
    codigos: set[str] = set()
    for df in dfs:
        if df is not None and not df.empty:
            encontrados = df.loc[df["CNPJ_CIA"].eq(CNPJ_ALVO), "CD_CVM"].dropna().astype(str)
            codigos.update(encontrados.tolist())
    if not codigos:
        return None
    if len(codigos) > 1:
        aviso(f"Mais de um CD_CVM encontrado para o CNPJ: {sorted(codigos)}; usando o primeiro.")
    return sorted(codigos)[0]


def carregar_ano(tipo: str, ano: int) -> tuple[pd.DataFrame, str | None]:
    """Baixa um ano, filtra pelo CNPJ e retorna as demonstrações disponíveis."""
    url = (URL_DFP if tipo == "DFP" else URL_ITR).format(ano=ano)
    destino = PASTA_CACHE / f"{tipo.lower()}_{ano}.zip"
    zbytes = baixar_zip(url, destino)
    if zbytes is None:
        return pd.DataFrame(), None

    todos: list[pd.DataFrame] = []
    for chave, sufixo in DEMOS.items():
        # O arquivo é nomeado, por exemplo, dfp_cia_aberta_BPA_con_2025.csv.
        for escopo in ("con", "ind"):
            nome = f"{tipo.lower()}_cia_aberta_{sufixo}_{escopo}_{ano}.csv"
            df = ler_csv_do_zip(zbytes, nome)
            if df is None:
                continue
            df = normalizar(df)
            df = df[df["CNPJ_CIA"].eq(CNPJ_ALVO)].copy()
            if not df.empty:
                df["FONTE_TIPO"] = tipo
                df["DEMONSTRACAO"] = chave
                df["ESCOPO"] = "Consolidado" if escopo == "con" else "Individual"
                todos.append(df)

    if not todos:
        aviso(f"Nenhum dado da ENGIE encontrado no ZIP {tipo} {ano}.")
        return pd.DataFrame(), None
    combinado = pd.concat(todos, ignore_index=True)
    return combinado, localizar_codigo_cvm([combinado])


def escolher_versao(df: pd.DataFrame) -> pd.DataFrame:
    """Mantém a reapresentação mais recente por demonstração/período/conta."""
    if df.empty:
        return df
    chaves = ["DEMONSTRACAO", "ESCOPO", "DT_REFER", "DT_FIM_EXERC", "CD_CONTA", "ORDEM_EXERC"]
    return (
        df.sort_values(chaves + ["VERSAO"])
        .drop_duplicates(chaves, keep="last")
        .sort_values(["DEMONSTRACAO", "ESCOPO", "DT_FIM_EXERC", "CD_CONTA"])
    )


def rotulo_periodo(row: pd.Series) -> str:
    def data(col: str) -> str:
        valor = row.get(col)
        return valor.strftime("%Y-%m-%d") if pd.notna(valor) else "sem-data"

    unidade = str(row.get("ESCALA_MOEDA") or "")
    return f"Ref {data('DT_REFER')} / Fim {data('DT_FIM_EXERC')} | {row['FONTE_TIPO']} v{int(row['VERSAO'])} | {row['ESCOPO']} | {unidade}"


def preparar_aba(df: pd.DataFrame) -> pd.DataFrame:
    """Converte a tabela longa da CVM em contas nas linhas e períodos nas colunas."""
    if df.empty:
        return pd.DataFrame(columns=["CD_CONTA", "DS_CONTA"])
    df = escolher_versao(df.copy())
    df["PERIODO"] = df.apply(rotulo_periodo, axis=1)

    # Caso exista mais de uma linha para a mesma conta/período, preserva a primeira
    # após a deduplicação por ordem original e informa a ambiguidade no terminal.
    duplicadas = df.duplicated(["CD_CONTA", "DS_CONTA", "PERIODO"], keep=False)
    if duplicadas.any():
        aviso(f"Há {int(duplicadas.sum())} linhas duplicadas na demonstração {df['DEMONSTRACAO'].iloc[0]}; mantendo a primeira.")
    df = df.drop_duplicates(["CD_CONTA", "DS_CONTA", "PERIODO"], keep="first")
    larga = df.pivot(index=["CD_CONTA", "DS_CONTA"], columns="PERIODO", values="VL_CONTA").reset_index()
    larga.columns.name = None
    return larga


def escrever_excel(dados: pd.DataFrame, caminho: str) -> dict[str, int]:
    contagem: dict[str, int] = {}
    with pd.ExcelWriter(caminho, engine="openpyxl") as writer:
        for demo in DEMOS:
            aba = preparar_aba(dados[dados["DEMONSTRACAO"].eq(demo)]) if not dados.empty else pd.DataFrame()
            if aba.empty:
                aviso(f"Sem dados para a aba {demo}; a aba será criada mesmo assim.")
                aba = pd.DataFrame(columns=["CD_CONTA", "DS_CONTA"])
            nome_aba = demo[:31]
            aba.to_excel(writer, sheet_name=nome_aba, index=False, startrow=2)
            ws = writer.book[nome_aba]
            ws.cell(row=1, column=1, value="Fonte: dados abertos oficiais da CVM; valores conforme ESCALA_MOEDA informada em cada coluna.")
            ws.cell(row=1, column=1).font = Font(italic=True)
            ws.cell(row=1, column=1).alignment = Alignment(wrap_text=True)
            ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(2, aba.shape[1]))
            ws.freeze_panes = "C4"
            ws.auto_filter.ref = ws.dimensions
            for cell in ws[3]:
                cell.font = Font(bold=True)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            ws.column_dimensions["A"].width = 18
            ws.column_dimensions["B"].width = 48
            for col in range(3, ws.max_column + 1):
                ws.column_dimensions[ws.cell(row=3, column=col).column_letter].width = 24
            contagem[demo] = max(0, len(aba))
    return contagem


def main() -> None:
    PASTA_CACHE.mkdir(exist_ok=True)
    ano_atual = datetime.now().year
    anos_dfp: list[int] = []
    partes: list[pd.DataFrame] = []
    codigo_cvm: str | None = None

    # Procura os cinco anos anuais mais recentes existentes, começando pelo ano anterior.
    ano = ano_atual
    while len(anos_dfp) < ANOS_ANUAIS and ano >= ano_atual - 10:
        df, codigo = carregar_ano("DFP", ano)
        if codigo:
            codigo_cvm = codigo_cvm or codigo
        if not df.empty:
            anos_dfp.append(ano)
            partes.append(df)
        ano -= 1

    # Busca ITRs do exercício corrente; se ainda não houver arquivo, emite aviso e segue.
    df_itr, codigo = carregar_ano("ITR", ANO_INICIAL_ITR)
    if codigo:
        codigo_cvm = codigo_cvm or codigo
    if not df_itr.empty:
        partes.append(df_itr)

    if not partes:
        raise SystemExit("Nenhum dado foi encontrado. Verifique o CNPJ, a conexão e as URLs da CVM.")

    dados = pd.concat(partes, ignore_index=True)
    dados = dados[dados["CNPJ_CIA"].eq(CNPJ_ALVO)].copy()
    dados = escolher_versao(dados)

    if codigo_cvm:
        print(f"CD_CVM confirmado pelo CNPJ {CNPJ_ALVO}: {codigo_cvm}")
    else:
        aviso("Não foi possível confirmar CD_CVM; a filtragem foi feita pelo CNPJ.")
    print(f"DFPs carregadas: {sorted(anos_dfp)}")
    print(f"ITR pesquisado: {ANO_INICIAL_ITR}")
    print(f"Registros contábeis carregados: {len(dados):,}".replace(",", "."))

    contagem = escrever_excel(dados, NOME_SAIDA)
    print(f"Arquivo criado: {NOME_SAIDA}")
    print("Linhas exportadas por aba:")
    for demo, quantidade in contagem.items():
        print(f"  {demo}: {quantidade:,}".replace(",", "."))


if __name__ == "__main__":
    main()
