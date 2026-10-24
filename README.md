# Dossiê de auditoria — ENGIE Brasil Energia S.A. (exercício 2025)

**Matrícula:** `222024004` · **Trabalho individual** · **Entrega:** 25/10/2026

> Trabalho acadêmico. Não é auditoria real nem opinião profissional. Não houve contato com a companhia, auditor, clientes ou fornecedores. A base de 500.000 registros é **SINTÉTICA**: o saldo de referência vem das demonstrações públicas, mas os registros, atributos e erros são fictícios.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `dossie/` | PDF e Markdown do dossiê completo |
| `papeis_trabalho/` | PT-EC e PT-200 a PT-600 |
| `base_simulada/` | CSV comprimido, dicionário, conciliação, erros e manifesto |
| `codigo/` | Extração CVM e geração da base |
| `docs/` | Fontes, matriz, método, normas e programas |
| `fontes/` | Links e documentos públicos usados |
| `planilhas/` | Cálculos e análises editáveis |
| `saidas/` | Resultados reproduzíveis |

## Companhia

ENGIE Brasil Energia S.A.; CNPJ 02.474.103/0001-19; Código CVM 17329; código B3 EGIE3; nome anterior Tractebel Energia S.A.

## Reprodução

```bash
pip install pandas numpy requests openpyxl
python codigo/01_gerar_base.py
python codigo/02_extrair_demonstracoes_cvm.py
```

A geração da base cria 500.000 registros e concilia o valor contábil líquido ao saldo consolidado de R$ 28.567.889 mil. O arquivo CSV completo está comprimido para facilitar o versionamento.

## Classificação dos procedimentos

Cada procedimento está identificado como realizado com evidência pública, planejado por falta de acesso ou simulado para fins didáticos. Confirmações, entrevistas, inspeções físicas e acessos a sistemas não foram realizados.

