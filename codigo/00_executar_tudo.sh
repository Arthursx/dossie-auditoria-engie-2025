#!/usr/bin/env bash
set -euo pipefail
python codigo/01_gerar_base.py
python codigo/02_extrair_demonstracoes_cvm.py
