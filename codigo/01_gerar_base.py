#!/usr/bin/env python3
"""Gera uma população SINTÉTICA de imobilizado para fins acadêmicos.

Importante:
- Os registros gerados não são registros reais da ENGIE.
- O saldo de conciliação é o saldo contábil consolidado divulgado pela ENGIE
  em 31/12/2025: R$ 28.567.889 mil.
- Fonte: Relatório da Administração e Demonstrações Financeiras 2025/2024,
  balanço patrimonial consolidado, p. 65, Nota 10 - Imobilizado, p. 107.
"""

from __future__ import annotations

import csv
import hashlib
import json
import random
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP, getcontext
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------- PARÂMETROS ---------------------------
N_REGISTROS = 500_000
SEMENTE = 20251001
SALDO_IMOBILIZADO_MIL = Decimal("28567889.000000")  # R$ mil
DATA_BASE = date(2025, 12, 31)
PASTA_SAIDA = Path("base_simulada")
NOME_BASE = "imobilizado_sintetico_500k.csv"
NOME_ERROS = "erros_inseridos.csv"
NOME_DICIONARIO = "dicionario_variaveis.csv"
NOME_CONCILIACAO = "conciliacao_imobilizado.csv"
NOME_MANIFESTO = "manifesto_geracao.json"

getcontext().prec = 28

CLASSES = np.array([
    "Usinas hidrelétricas",
    "Usinas termelétricas",
    "Parques eólicos",
    "Parques solares",
    "Linhas e subestações",
    "Máquinas e equipamentos",
    "Edificações e instalações",
    "Tecnologia da informação",
    "Veículos e embarcações",
    "Móveis e utensílios",
], dtype=object)

UNIDADES = np.array([
    "UHE-SINTETICA-01", "UHE-SINTETICA-02", "UTE-SINTETICA-01",
    "EOL-SINTETICA-01", "EOL-SINTETICA-02", "SOL-SINTETICA-01",
    "TRANSMISSAO-SINTETICA-01", "CORPORATIVO-SINTETICO-01",
], dtype=object)

VIDAS_POR_CLASSE = {
    "Usinas hidrelétricas": (25, 50),
    "Usinas termelétricas": (15, 35),
    "Parques eólicos": (15, 25),
    "Parques solares": (15, 30),
    "Linhas e subestações": (20, 40),
    "Máquinas e equipamentos": (8, 25),
    "Edificações e instalações": (20, 50),
    "Tecnologia da informação": (3, 8),
    "Veículos e embarcações": (5, 15),
    "Móveis e utensílios": (5, 15),
}

DICIONARIO = [
    ("id_ativo", "Identificador sintético único, salvo erro didático documentado.", "texto", "Não"),
    ("status_base", "Marcador de que a linha pertence à população sintética.", "texto", "Não"),
    ("empresa_sintetica", "Entidade fictícia para separar os dados sintéticos de dados reais.", "texto", "Não"),
    ("unidade_operacional_sintetica", "Unidade operacional fictícia.", "texto", "Não"),
    ("classe_ativo", "Classe sintética do bem do imobilizado.", "texto", "Não"),
    ("descricao_sintetica", "Descrição gerada para o bem; não representa cadastro real.", "texto", "Não"),
    ("data_aquisicao", "Data sintética de aquisição do bem.", "data", "Não"),
    ("data_entrada_operacao", "Data sintética de entrada em operação.", "data", "Não"),
    ("valor_original_mil", "Custo original sintético, em milhares de reais.", "decimal R$ mil", "Sim"),
    ("valor_residual_mil", "Valor residual sintético, em milhares de reais.", "decimal R$ mil", "Sim"),
    ("vida_util_anos", "Vida útil econômica sintética em anos.", "inteiro", "Não"),
    ("depreciacao_acumulada_mil", "Depreciação acumulada sintética, em milhares de reais.", "decimal R$ mil", "Sim"),
    ("depreciacao_ano_2025_mil", "Despesa de depreciação sintética de 2025, em milhares de reais.", "decimal R$ mil", "Sim"),
    ("valor_contabil_liquido_mil", "Valor contábil líquido sintético, em milhares de reais.", "decimal R$ mil", "Sim"),
    ("indicador_impairment", "Indicador sintético para testes de impairment.", "S/N", "Não"),
    ("localizacao_sintetica", "Localização fictícia do bem.", "texto", "Não"),
]


def data_aleatoria(rng: random.Random, inicio: date, fim: date) -> date:
    dias = (fim - inicio).days
    return inicio + timedelta(days=rng.randint(0, dias))


def decimal_str(valor: float | Decimal) -> str:
    """Formata sem separador de milhar e com seis casas decimais."""
    return f"{Decimal(str(valor)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP):f}"


def hash_arquivo(caminho: Path) -> str:
    sha = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            sha.update(bloco)
    return sha.hexdigest()


def gerar_base() -> pd.DataFrame:
    rng_np = np.random.default_rng(SEMENTE)
    rng_py = random.Random(SEMENTE)

    # Cada linha representa um bem sintético individual; IDs e atributos variam.
    classes = rng_np.choice(CLASSES, size=N_REGISTROS)
    unidades = rng_np.choice(UNIDADES, size=N_REGISTROS)
    custos = rng_np.lognormal(mean=3.25, sigma=1.15, size=N_REGISTROS)
    custos = np.maximum(custos, 0.10)

    vidas = np.array([
        rng_py.randint(*VIDAS_POR_CLASSE[classe]) for classe in classes
    ], dtype=np.int16)

    # Fração líquida positiva para que o valor contábil líquido seja menor que o custo.
    frac_liquida = rng_np.uniform(0.08, 0.96, size=N_REGISTROS)
    liquidos = custos * frac_liquida

    # Escala exata da população para o saldo contábil consolidado divulgado.
    alvo = float(SALDO_IMOBILIZADO_MIL)
    liquidos *= alvo / liquidos.sum()
    custos *= alvo / liquidos.sum() if False else 1.0

    # Garante custo maior que o valor líquido após a escala.
    custos = np.maximum(custos, liquidos + 0.01)
    depreciacao = custos - liquidos
    residuais = np.minimum(custos * rng_np.uniform(0.00, 0.10, size=N_REGISTROS), liquidos * 0.25)
    depreciacao_2025 = np.minimum(depreciacao * rng_np.uniform(0.02, 0.10, size=N_REGISTROS), liquidos * 0.20)

    datas_aquisicao: list[str] = []
    datas_operacao: list[str] = []
    for _ in range(N_REGISTROS):
        aquisicao = data_aleatoria(rng_py, date(1990, 1, 1), date(2025, 6, 30))
        operacao = data_aleatoria(rng_py, aquisicao, date(2025, 12, 31))
        datas_aquisicao.append(aquisicao.isoformat())
        datas_operacao.append(operacao.isoformat())

    ids = [f"BEM-SINT-{i:07d}" for i in range(1, N_REGISTROS + 1)]
    base = pd.DataFrame({
        "id_ativo": ids,
        "status_base": "SINTETICO - USO DIDATICO - NAO REAL",
        "empresa_sintetica": "ENGIE-ENTIDADE-SINTETICA",
        "unidade_operacional_sintetica": unidades,
        "classe_ativo": classes,
        "descricao_sintetica": [f"Bem sintético {classe} {i:07d}" for i, classe in enumerate(classes, 1)],
        "data_aquisicao": datas_aquisicao,
        "data_entrada_operacao": datas_operacao,
        "valor_original_mil": custos,
        "valor_residual_mil": residuais,
        "vida_util_anos": vidas,
        "depreciacao_acumulada_mil": depreciacao,
        "depreciacao_ano_2025_mil": depreciacao_2025,
        "valor_contabil_liquido_mil": liquidos,
        "indicador_impairment": rng_np.choice(["S", "N"], size=N_REGISTROS, p=[0.04, 0.96]),
        "localizacao_sintetica": [f"LOCAL-SINT-{i % 250:03d}" for i in range(N_REGISTROS)],
    })

    # Arredondamento controlado e ajuste residual para conciliar exatamente ao alvo.
    monetarias = [
        "valor_original_mil", "valor_residual_mil", "depreciacao_acumulada_mil",
        "depreciacao_ano_2025_mil", "valor_contabil_liquido_mil",
    ]
    for coluna in monetarias:
        base[coluna] = base[coluna].astype(float).round(6)

    soma = Decimal(str(base["valor_contabil_liquido_mil"].sum())).quantize(Decimal("0.000001"))
    diferenca = SALDO_IMOBILIZADO_MIL - soma
    base.loc[N_REGISTROS - 1, "valor_contabil_liquido_mil"] = float(
        Decimal(str(base.loc[N_REGISTROS - 1, "valor_contabil_liquido_mil"])) + diferenca
    )
    # Mantém a identidade custo - depreciação = líquido na linha ajustada.
    base.loc[N_REGISTROS - 1, "depreciacao_acumulada_mil"] = round(
        base.loc[N_REGISTROS - 1, "valor_original_mil"] - base.loc[N_REGISTROS - 1, "valor_contabil_liquido_mil"], 6
    )

    return base


def inserir_erros_didaticos(base: pd.DataFrame) -> pd.DataFrame:
    """Insere apenas inconsistências de teste e registra cada uma delas."""
    erros = []

    def registrar(linha: int, campo: str, antes: object, depois: object, tipo: str, teste: str) -> None:
        erros.append({
            "id_ativo": base.at[linha, "id_ativo"],
            "linha_zero_based": linha,
            "tipo_erro": tipo,
            "campo": campo,
            "valor_original": antes,
            "valor_inserido": depois,
            "procedimento_que_deve_identificar": teste,
        })

    # Erros de metadados/controle; não alteram a conciliação do saldo líquido.
    linha = 100
    antes = base.at[linha, "vida_util_anos"]
    base.at[linha, "vida_util_anos"] = 0
    registrar(linha, "vida_util_anos", antes, 0, "vida útil inválida", "teste de estimativa/depreciação")

    linha = 200
    antes = base.at[linha, "data_entrada_operacao"]
    base.at[linha, "data_entrada_operacao"] = "1980-01-01"
    registrar(linha, "data_entrada_operacao", antes, "1980-01-01", "data anterior à aquisição", "teste de datas")

    linha = 300
    antes = base.at[linha, "id_ativo"]
    base.at[linha, "id_ativo"] = base.at[299, "id_ativo"]
    registrar(linha, "id_ativo", antes, base.at[linha, "id_ativo"], "ID duplicado", "teste de unicidade")

    linha = 400
    antes = base.at[linha, "indicador_impairment"]
    base.at[linha, "indicador_impairment"] = "X"
    registrar(linha, "indicador_impairment", antes, "X", "domínio inválido", "teste de domínio")

    return pd.DataFrame(erros)


def escrever_dicionario() -> None:
    with (PASTA_SAIDA / NOME_DICIONARIO).open("w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(["variavel", "descricao", "tipo", "monetaria"])
        writer.writerows(DICIONARIO)


def escrever_conciliacao(base: pd.DataFrame) -> None:
    total = Decimal(str(base["valor_contabil_liquido_mil"].sum())).quantize(Decimal("0.000001"))
    diferenca = total - SALDO_IMOBILIZADO_MIL
    linhas = [
        ["Fonte", "ENGIE Brasil Energia S.A. - DFs 2025/2024, balanço consolidado p. 65, Nota 10 p. 107"],
        ["Data-base", "31/12/2025"],
        ["Unidade", "R$ mil"],
        ["Saldo contábil consolidado divulgado", decimal_str(SALDO_IMOBILIZADO_MIL)],
        ["Quantidade de registros sintéticos", str(len(base))],
        ["Total da população sintética", decimal_str(total)],
        ["Diferença", decimal_str(diferenca)],
        ["Status", "CONCILIADO" if diferenca == 0 else "REVISAR"],
        ["Natureza", "Todos os registros são sintéticos e não representam bens reais da ENGIE."],
    ]
    with (PASTA_SAIDA / NOME_CONCILIACAO).open("w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(["item", "valor"])
        writer.writerows(linhas)


def main() -> None:
    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)
    base = gerar_base()
    erros = inserir_erros_didaticos(base)

    caminho_base = PASTA_SAIDA / NOME_BASE
    base.to_csv(caminho_base, index=False, sep=";", decimal=".", encoding="utf-8", float_format="%.6f")
    erros.to_csv(PASTA_SAIDA / NOME_ERROS, index=False, sep=";", encoding="utf-8")
    escrever_dicionario()
    escrever_conciliacao(base)

    manifesto = {
        "natureza_dos_dados": "SINTETICOS - NAO SAO REGISTROS REAIS DA ENGIE",
        "companhia_de_referencia": "ENGIE Brasil Energia S.A.",
        "cnpj": "02.474.103/0001-19",
        "data_base": "2025-12-31",
        "conta": "Imobilizado consolidado",
        "saldo_contabil_r_mil": str(SALDO_IMOBILIZADO_MIL),
        "quantidade_registros": N_REGISTROS,
        "semente": SEMENTE,
        "fonte": "https://www.engie.com.br/wp-content/uploads/2026/02/DF-EBE-31.12.2025-vs_06_03-reap.pdf",
        "referencia_fonte": "Balanço consolidado p. 65 e Nota 10 - Imobilizado p. 107",
        "arquivo_base_sha256": hash_arquivo(caminho_base),
        "erros_didaticos_inseridos": len(erros),
    }
    (PASTA_SAIDA / NOME_MANIFESTO).write_text(
        json.dumps(manifesto, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    total = Decimal(str(base["valor_contabil_liquido_mil"].sum())).quantize(Decimal("0.000001"))
    print("Base sintética criada com sucesso.")
    print(f"Arquivo: {caminho_base}")
    print(f"Registros: {len(base):,}".replace(",", "."))
    print(f"Total líquido sintético: R$ {total:,.6f} mil".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Saldo de referência: R$ {SALDO_IMOBILIZADO_MIL:,.6f} mil".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Diferença: R$ {total - SALDO_IMOBILIZADO_MIL:,.6f} mil")
    print(f"Erros didáticos registrados: {len(erros)}")
    print(f"Dicionário: {PASTA_SAIDA / NOME_DICIONARIO}")
    print(f"Conciliação: {PASTA_SAIDA / NOME_CONCILIACAO}")


if __name__ == "__main__":
    main()
