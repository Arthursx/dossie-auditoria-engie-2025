# Dossiê de Auditoria — ENGIE Brasil Energia S.A.

**Trabalho didático — exercício encerrado em 31/12/2025**  
**Aluno/matrícula:** `[PREENCHER]`  
**Preparador:** `[PREENCHER]`  
**Data de preparação:** `[PREENCHER]`  
**Data de corte das fontes:** `[PREENCHER]`  
**Status:** minuta acadêmica para revisão do aluno

> **Natureza do trabalho.** Este dossiê é acadêmico e não representa uma auditoria independente, uma opinião profissional ou uma comunicação emitida em nome da UnB. Procedimentos foram classificados como **R — realizado com evidência pública**, **P — planejado por falta de acesso** ou **S — simulado para fins didáticos**.

## 1. Identificação da companhia e escopo

A companhia analisada é a **ENGIE Brasil Energia S.A.**, CNPJ 02.474.103/0001-19, Código CVM 17329. O Formulário Cadastral de 2025 informa que o nome empresarial anterior era **Tractebel Energia S.A.**, com início do nome atual em 14/07/2016. A companhia é do setor de energia elétrica e possui ações ordinárias negociadas na B3 sob o código **EGIE3**. O código `ENGI11` não foi utilizado como identificador da companhia, pois a filtragem dos dados contábeis foi feita pelo CNPJ e o cadastro consultado da B3 apresenta EGIE3.

O escopo compreende as demonstrações financeiras anuais consolidadas e individuais de 2025, os comparativos de 2024, as notas explicativas, o relatório do auditor independente e informações públicas da CVM, B3 e área de Relações com Investidores. Os procedimentos internos que dependeriam de confirmação, entrevista, inspeção física, acesso a sistemas ou documentos não públicos não foram tratados como realizados.

## 2. Fontes e convenção de evidências

| Código | Fonte/documento | Exercício | Uso no dossiê | Classificação |
|---|---|---:|---|---|
| F-001 | Relatório da Administração e Demonstrações Financeiras da ENGIE, páginas 1–203 | 2025 e 2024 | Demonstrações, notas, auditoria e governança | R |
| F-002 | Formulário Cadastral da ENGIE Brasil Energia S.A. | 2025 | CNPJ, nome anterior, CVM, EGIE3 e auditor | R |
| F-003 | Dados Abertos CVM — DFP | 2021–2025 | BPA, BPP, DRE, DFC, DMPL, DVA e DRA | R |
| F-004 | Dados Abertos CVM — ITR | exercício corrente | Verificação de disponibilidade de ITR | R |
| F-005 | Cadastro da companhia na B3 | 2025/consulta | Código, CNPJ, setor e dados cadastrais | R |
| F-006 | Base `imobilizado_sintetico_500k.csv` | 2025 | População sintética para amostragem | S |
| F-007 | Código `gerar_base_imobilizado_engie.py` | 2025 | Reprodução da base e dos testes | S |

**Referência principal:** [F-001 — DFs 2025/2024](https://www.engie.com.br/wp-content/uploads/2026/02/DF-EBE-31.12.2025-vs_06_03-reap.pdf). As páginas citadas neste dossiê correspondem à paginação impressa do documento; o aluno deve registrar a data efetiva de acesso antes da entrega.

## 3. Dados contábeis relevantes

Os valores abaixo estão em **R$ mil**, conforme as demonstrações da companhia.

| Conta consolidada | Nota | 31/12/2025 | 31/12/2024 | Variação aproximada |
|---|---:|---:|---:|---:|
| Caixa e equivalentes de caixa | 3 | 3.358.552 | 3.958.758 | -15,2% |
| Contas a receber de clientes | 4 | 1.322.661 | 1.174.405 | 12,6% |
| Ativo financeiro de concessão | 6 | 3.160.294 | 3.070.039 | 2,9% |
| Ativo de contrato | 7 | 8.710.991 | 7.028.394 | 23,9% |
| Investimentos | 9 | 1.155.320 | 1.250.625 | -7,6% |
| Imobilizado | 10 | 28.567.889 | 25.186.537 | 13,4% |
| Intangível | 11 | 5.369.554 | 5.088.963 | 5,5% |
| Total do ativo | — | 55.312.909 | 50.112.301 | 10,4% |

O imobilizado foi selecionado para a base simulada por possuir saldo elevado, representar aproximadamente 51,6% do ativo consolidado e estar diretamente relacionado à atividade operacional de geração e transmissão de energia. A seleção também permite testar existência, direitos, avaliação, depreciação, baixas, vida útil e impairment.

## 4. Classificação das evidências

- **R — Realizado com evidência pública:** leitura das demonstrações, notas, relatório do auditor, Formulário Cadastral, dados da CVM e cadastro público da B3; cálculos reproduzíveis feitos a partir desses documentos.
- **P — Planejado por falta de acesso:** confirmação de saldos, inspeção física, entrevistas, análise de controles internos, acesso a ERP, testes de autorização e consulta a advogados ou prestadores.
- **S — Simulado para fins didáticos:** geração da população de 500.000 linhas, inserção controlada de exceções, amostragem sobre a população sintética e análise de resultados da simulação.

## PT EC — Estrutura Conceitual

**Norma/itens:** NBC TA Estrutura Conceitual.  
**Objetivo:** caracterizar o trabalho, seus usuários, objeto, critérios, responsabilidades, evidências e nível de asseguração.

O objeto é a informação contábil-financeira da ENGIE Brasil Energia referente ao exercício de 2025. Os critérios são as práticas contábeis aplicáveis e as divulgações apresentadas nas demonstrações financeiras. Os usuários previstos são o professor e o aluno, para fins acadêmicos. A administração é responsável pela elaboração das demonstrações; o auditor independente seria responsável por obter segurança razoável e emitir relatório, mas este dossiê não emite opinião.

A auditoria é um trabalho de asseguração razoável, com avaliação de riscos e obtenção de evidência suficiente e apropriada. Não se confunde com revisão, que normalmente proporciona asseguração limitada, nem com procedimentos previamente acordados, que resultam em achados sem opinião de asseguração. Este trabalho didático utiliza evidência pública e dados sintéticos, portanto suas conclusões são limitadas ao escopo acadêmico.

**Conclusão:** o objeto e os critérios são identificáveis, mas não estão presentes todas as condições de uma auditoria real, especialmente acesso à administração, controles e evidências internas. **Classificação:** R para documentos públicos; P para condições internas.

## PT 200 — Objetivos gerais

**Riscos:** ameaça à independência, viés de confirmação, excesso de confiança nos documentos públicos e confusão entre análise acadêmica e auditoria profissional.

Foram definidos os princípios de integridade, objetividade, competência, confidencialidade e comportamento profissional. O ceticismo será aplicado questionando variações relevantes, estimativas, transações com partes relacionadas e informações não corroboradas. O julgamento profissional será documentado nos PT 315, 320, 330 e 540.

O risco de auditoria é tratado como combinação de risco inerente, risco de controle e risco de detecção. A segurança razoável não é segurança absoluta. As fontes públicas não permitem testar integralmente controles, completude de passivos ou existência física de ativos.

**Conclusão:** os objetivos gerais foram convertidos em procedimentos específicos, mas a obtenção de segurança razoável não é afirmada neste trabalho. **Classificação:** R/P.

## PT 210 — Termos do trabalho

**Documento:** minuta didática de carta de contratação.

**Objetivo e alcance:** examinar, para fins acadêmicos, as demonstrações de 2025, comparativos, notas e relatório do auditor da ENGIE, com foco nos riscos relevantes e no imobilizado.

**Responsabilidades:** a administração seria responsável pelas demonstrações, controles, acesso às informações e representações; o auditor seria responsável pelo planejamento, execução, documentação e relatório; o aluno é responsável apenas pela preparação deste estudo.

**Precondições:** há uma estrutura contábil identificável e demonstrações públicas. Não há contratação real, comunicação com a companhia ou aceitação formal pela administração. Não existe carta de contratação real. **Conclusão:** a carta é uma simulação acadêmica e não comprova a aceitação de um trabalho profissional. **Classificação:** S/P.

## PT 220 — Gestão da qualidade

Foram previstos direção do trabalho, supervisão, revisão pelo próprio preparador, consulta técnica documentada e controle de versões. Riscos à qualidade incluem uso de dados públicos incompletos, geração de dados sintéticos com distribuição artificial, erro de transcrição, conflito entre fonte impressa e CSV e ausência de revisão independente.

Medidas adotadas: uso de fonte oficial, código reproduzível, manifesto com hash da base, pasta de evidências, referências cruzadas e separação entre R e S. Não foi simulada assinatura ou revisão de terceiro. **Conclusão:** controles de qualidade foram planejados e parcialmente executados pelo próprio aluno; revisão independente permanece pendente. **Classificação:** R/P/S.

## PT 230 — Documentação

**Índice:** EC, 200, 210, 220, 230, 240, 250, 260, 265, 300, 315, 320, 330, 402, 450, 500, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580, 600, programas e anexos.

**Convenção:** F = fonte; PT = papel de trabalho; PGM = programa; B = base; A = análise; C = conclusão. Exemplo: `PT-530-B01` é a população usada na amostragem.

**Referências cruzadas:** PT 315 liga-se a PT 320 e PT 330; PT 320 liga-se a PT 450 e PT 530; PT 500 liga-se a F-001 e B-001; PT 530 liga-se a B-001, `erros_inseridos.csv` e `conciliacao_imobilizado.csv`.

**Controle de versões:** versão 1.0 = minuta inicial; alterações devem ser registradas no README e no manifesto. Os arquivos devem ser preservados em repositório com acesso ao professor. **Classificação:** R/S.

## PT 240 — Fraude

Foram considerados riscos de reconhecimento inadequado de receita de energia, lançamento manual próximo ao encerramento, manipulação de estimativas de vida útil e impairment, ocultação de passivos e burla de controles pela administração.

**Procedimentos R:** leitura da receita, notas de partes relacionadas, instrumentos financeiros, provisões e eventos subsequentes.  
**Procedimentos P:** obter diário completo, testar lançamentos manuais, examinar usuários com acesso privilegiado, investigar transações incomuns e confirmar cut-off com documentos internos.  
**Procedimentos S:** aplicar testes de unicidade, domínio e datas na população sintética; quatro exceções foram inseridas e registradas.

**Conclusão:** os documentos públicos não sustentam conclusão sobre ausência de fraude. O risco de burla da administração permanece significativo e exige procedimentos internos planejados. **Classificação:** R/P/S.

## PT 250 — Leis e regulamentos

O ambiente da ENGIE envolve regulação do setor elétrico, concessões, obrigações fiscais, ambientais, trabalhistas, societárias e regras da CVM/B3. Os principais reflexos contábeis estão em concessões, provisões, tributos, obrigações regulatórias e eventos subsequentes.

**Procedimentos R:** ler notas 6, 7, 15, 17 e 18, além do Formulário Cadastral e informações públicas.  
**Procedimentos P:** obter matriz legal da companhia, consultar assessores jurídicos, examinar licenças, autos regulatórios e evidências de cumprimento.  
**Comunicação planejada:** indícios de descumprimento seriam comunicados à governança, sem contato real neste trabalho.

**Conclusão:** não foram identificados, apenas pela documentação pública analisada, elementos suficientes para afirmar descumprimento. Isso não equivale a concluir que não existam contingências. **Classificação:** R/P.

## PT 260 — Comunicação com a governança

A comunicação didática deve informar: alcance; época; riscos significativos; materialidade; independência; limitações de acesso; uso de dados sintéticos; ausência de confirmações e inspeções; principais julgamentos; exceções simuladas; e assuntos que exigiriam consulta.

A comunicação não foi enviada à companhia nem ao auditor. Foi preparada apenas como minuta acadêmica. **Conclusão:** a comunicação atende ao formato solicitado, mas não produz efeitos perante a governança. **Classificação:** S/P.

## PT 265 — Deficiências de controle

| Natureza | Condição | Critério | Causa/efeito | Recomendação | Status |
|---|---|---|---|---|---|
| Hipótese | Lançamentos manuais e cut-off podem não ter revisão suficiente | Controle de autorização e revisão | Pode antecipar receita | Revisão independente e relatório de exceções | P |
| Hipótese | Cadastro de imobilizado pode conter campos incompletos | Integridade do cadastro | Pode afetar depreciação e existência | Validações obrigatórias e inventário periódico | P |
| Simulada | Vida útil igual a zero | Domínio esperado positivo | Afeta cálculo de depreciação | Bloqueio de cadastro | S |
| Simulada | ID duplicado | Identificador único | Pode duplicar população | Restrição de unicidade | S |
| Não constatada | Deficiência real de controle da ENGIE | — | Não há acesso a controles internos | Não apresentar como achado real | R/P |

**Conclusão:** somente as duas últimas linhas simuladas foram identificadas na base sintética; as duas primeiras são hipóteses de risco, não constatações da companhia.

## PT 300 — Planejamento

**Estratégia:** priorizar imobilizado, ativo de contrato, concessões, receita, instrumentos financeiros, provisões, continuidade e consolidação. A fase pública inclui leitura, extração de saldos, análise de variações e conciliação. A fase interna é planejada, não executada.

**Cronograma didático:** documentação e fontes; análise de riscos/materialidade; geração e validação da base; amostragem; programas de auditoria; redação e revisão final.

**Alterações:** a escolha do imobilizado foi mantida por sua relevância e pela possibilidade de criar registros individuais sintéticos; a DFC pelo método direto foi mantida como aba vazia quando a CVM não apresentou dados para a companhia/período.

## PT 315 — Identificação e avaliação de riscos

| Área | Afirmações | Risco | Avaliação | Resposta |
|---|---|---|---|---|
| Imobilizado | Existência, direitos, avaliação, apresentação | Bem inexistente, depreciação/vida útil incorreta, impairment não reconhecido | Alto | PT 330, PT 530, PT 540 |
| Ativo de contrato | Existência, avaliação, cut-off | Mensuração inadequada de contratos/concessões | Alto | Leitura da Nota 7 e testes internos planejados |
| Receita | Ocorrência, cut-off, exatidão | Reconhecimento antecipado ou incompleto | Alto | Teste de lançamentos e cut-off planejado |
| Caixa | Existência, direitos | Saldo ou restrição não identificado | Médio | Conciliação pública; confirmação planejada |
| Provisões | Completude, avaliação | Passivos/litígios não registrados | Alto | Nota 17; circularização jurídica planejada |
| Partes relacionadas | Completude, apresentação | Operações não divulgadas | Alto | Nota 25 e mapeamento societário |
| Grupo | Apresentação, consolidação | Componente ou eliminação incorreta | Alto | PT 600 |
| Continuidade | Apresentação | Liquidez, dívida e eventos adversos | Médio/alto | PT 570 |

A compreensão de TI e controles internos foi limitada às divulgações públicas. Não houve walkthrough, teste de acesso, teste de mudança de sistema ou inspeção de controles. **Classificação:** R/P.

## PT 320 — Materialidade

A materialidade deve ser finalizada pelo aluno após conferir a versão dos valores. Como cálculo didático inicial, foi escolhida a receita líquida de 2025, R$ 12.860.075 mil, por ser uma base relevante para uma companhia operacional de energia. Aplicando 0,5%:

- Materialidade global: **R$ 64.300,375 mil**;
- Materialidade para execução, a 75%: **R$ 48.225,281 mil**;
- Limite claramente trivial, a 5% da materialidade global: **R$ 3.215,019 mil**.

Esses percentuais são premissas acadêmicas, não parâmetros oficiais da ENGIE ou do auditor. Deve-se revisar a materialidade se houver alteração do entendimento da base, resultado, risco ou usuário. A materialidade do imobilizado é relevante porque o saldo de R$ 28.567.889 mil excede amplamente a materialidade global. **Classificação:** R, com julgamento S.

## PT 330 — Respostas aos riscos

| Risco | Teste de controle | Procedimento substantivo | Status |
|---|---|---|---|
| Vida útil incorreta | Revisar aprovação do cadastro | Recalcular depreciação em amostra | P/S |
| ID duplicado | Testar validação do sistema | Busca de duplicidade na base | S |
| Bem inexistente | Verificar controle de movimentação | Inspeção física e documentos | P |
| Impairment | Avaliar aprovação de indicadores | Sensibilidade de premissas | P/S |
| Receita antecipada | Revisar controle de cut-off | Testar documentos antes/depois do encerramento | P |
| Provisões incompletas | Avaliar revisão jurídica | Circularização e leitura de contratos | P |

A base sintética permitiu executar somente testes de dados sobre registros sintéticos, não testes sobre ativos reais.

## PT 402 — Organização prestadora de serviços

A companhia pode utilizar serviços terceirizados de tecnologia, folha, custódia, operação, manutenção ou processamento financeiro. A documentação pública não permite afirmar quais prestadores são relevantes para os controles das demonstrações.

**Planejamento:** identificar prestadores relevantes; solicitar relatório SOC/ISAE tipo 1 ou tipo 2; avaliar descrição, desenho, implementação e operação dos controles; testar controles complementares da entidade usuária; aplicar procedimentos alternativos se não houver relatório.

**Conclusão:** não foi identificado publicamente um prestador específico com evidência suficiente para conclusão. **Classificação:** R/P.

## PT 450 — Distorções

| ID | Origem | Valor | Natureza | Corrigida? | Tratamento |
|---|---|---:|---|---|---|
| D-001 | Base sintética — vida útil zero | Não quantificado | Classificação/cadastro | Não aplicável | Corrigir cadastro simulado |
| D-002 | Base sintética — data incompatível | Não quantificado | Integridade de dados | Não aplicável | Investigar data |
| D-003 | Base sintética — ID duplicado | Valor do registro | Existência/população | Não aplicável | Eliminar duplicidade no cadastro |
| D-004 | Base sintética — domínio `X` | Não quantificado | Validade | Não aplicável | Corrigir domínio |

Não foram projetadas distorções sintéticas para o saldo contábil. As exceções são falhas de dados de teste e não distorções atribuídas à ENGIE. Não há mapa de distorções reais não corrigidas. **Classificação:** S.

## PT 500 — Evidência

A evidência documental pública é relevante para saldos, políticas, divulgações e variações, mas tem limitações de confiabilidade para existência física, completude de passivos, operação de controles e direitos contratuais. A base sintética é adequada para testar o código de análise e amostragem, mas não prova a existência de ativos reais.

A conciliação do imobilizado foi feita entre o total da população sintética e o saldo consolidado de R$ 28.567.889 mil. O arquivo `conciliacao_imobilizado.csv` registra total, unidade, diferença e status. **Resultado:** diferença zero após ajuste residual controlado na última linha sintética. **Classificação:** R/S.

## PT 501 — Itens específicos

**Estoques:** a atividade da ENGIE não torna estoques o foco principal do ativo selecionado. Procedimentos de contagem, custeio e obsolescência seriam planejados se o saldo fosse relevante; não houve inspeção física.  
**Litígios:** a Nota 17 foi lida; confirmação com advogados e exame de processos são planejados.  
**Segmentos:** a Nota 26 foi considerada para entender geração/transmissão e apresentação por segmento; não foram reprocessados dados internos por segmento.

A conclusão de não materialidade de estoques, se adotada, deve ser confirmada pelo aluno na Nota 8 e demais divulgações. **Classificação:** R/P.

## PT 505 — Confirmações externas

Foi preparada, mas não enviada, uma minuta de confirmação para bancos, clientes, custodiantes e assessores jurídicos. O controle proposto inclui população, seleção, endereço independente, envio pelo auditor, respostas, diferenças e procedimentos alternativos.

Procedimentos alternativos planejados: examinar recebimentos posteriores, contratos, notas fiscais, extratos, documentos de concessão e decisões judiciais. Nenhuma confirmação foi apresentada como realizada. **Classificação:** P.

## PT 510 — Saldos iniciais

O caso foi tratado como auditoria inicial didática. Foram utilizados os comparativos de 2024 apresentados nas demonstrações de 2025 e as políticas contábeis divulgadas. O saldo de abertura do imobilizado consolidado é R$ 25.186.537 mil e o saldo de encerramento é R$ 28.567.889 mil.

Procedimentos planejados adicionais: ler relatório do auditor anterior; verificar se houve modificação de opinião; avaliar políticas e transição; examinar movimentos de aquisição, baixa e depreciação. A leitura pública não substitui os papéis de trabalho do auditor predecessor. **Classificação:** R/P.

## PT 520 — Procedimentos analíticos

A variação do imobilizado consolidado foi de aproximadamente 13,4%, de R$ 25.186.537 mil para R$ 28.567.889 mil. O total do ativo cresceu aproximadamente 10,4%. A conta, portanto, cresceu acima do ativo total e merece investigação.

O ativo de contrato cresceu aproximadamente 23,9%, enquanto contas a receber cresceram 12,6%. Essas variações são expectativas para procedimentos adicionais, não conclusões de erro. Procedimentos planejados: decompor aquisições e baixas; comparar CAPEX com fluxo de caixa; avaliar depreciação; investigar variações por classe e componente; relacionar crescimento a expansão e concessões.

**Classificação:** R para cálculo público; P para investigação interna.

## PT 530 — Amostragem

**População:** 500.000 registros da base sintética de imobilizado.  
**Unidade:** um bem sintético individual.  
**Valor da população:** R$ 28.567.889 mil.  
**Método:** seleção aleatória reprodutível por semente; seleção adicional dirigida dos maiores valores e das linhas com exceções conhecidas.  
**Risco:** risco amostral existe na seleção aleatória; a simulação não permite inferir sobre ativos reais.

Uma seleção acadêmica inicial pode usar 60 itens aleatórios, acrescidos de todos os itens de alto valor acima da materialidade para execução e das quatro linhas documentadas em `erros_inseridos.csv`. O tamanho deve ser justificado pelo risco e pela finalidade didática, e não apresentado como tamanho obrigatório da NBC TA.

Testes executados na população sintética: unicidade do ID, domínio do indicador de impairment, vida útil positiva e coerência entre datas. Foram encontradas quatro exceções: vida útil zero, data anterior à aquisição, ID duplicado e domínio `X`. **Classificação:** S.

## PT 540 — Estimativas contábeis

A estimativa selecionada é a vida útil e a depreciação do imobilizado. Os fatores relevantes são classe do ativo, data de entrada em operação, vida útil, valor residual, depreciação acumulada, indicadores de impairment e premissas de uso.

**Procedimentos públicos:** ler Nota 10, políticas contábeis e movimentação divulgada.  
**Procedimentos planejados:** comparar vida útil com laudos técnicos, manutenção, capacidade e uso; recalcular depreciação; avaliar valor residual; testar indicadores de impairment; realizar análise de sensibilidade.  
**Simulação:** a linha com vida útil zero foi identificada pelo teste de domínio. Isso não prova erro da companhia.

Uma sensibilidade didática pode alterar a vida útil de uma amostra sintética em 10% para observar impacto no valor contábil e na despesa, sem atribuir o resultado à ENGIE. **Classificação:** R/P/S.

## PT 550 — Partes relacionadas

A Nota 25 foi utilizada para mapear saldos, transações e remuneração da administração. O grupo, investimentos e transações com entidades relacionadas exigem atenção à completude e à divulgação.

Procedimentos planejados: comparar cadastro societário, atas, contratos, fornecedores/clientes relevantes, pagamentos, saldos e divulgações; pesquisar operações fora do curso normal; obter representação da administração. A documentação pública não permite concluir sobre a completude de partes relacionadas não divulgadas. **Classificação:** R/P.

## PT 560 — Eventos subsequentes

A data de corte deve ser registrada pelo aluno como a data da última consulta pública antes da entrega. A Nota 30 foi examinada para identificar eventos posteriores ao encerramento.

Procedimentos: consultar fatos relevantes, resultados posteriores, atas públicas e novas demonstrações; distinguir eventos que ajustam condições existentes em 31/12/2025 de eventos que apenas exigem divulgação. Não foram realizadas consultas internas nem obtidas representações específicas. **Classificação:** R/P.

## PT 570 — Continuidade operacional

Foram considerados caixa, fluxo de caixa, dívida, concessões a pagar, liquidez, obrigações e eventos adversos. A companhia apresentou ativo total consolidado de R$ 55.312.909 mil e passivos que devem ser analisados em conjunto com vencimentos e fluxos de caixa.

Procedimentos planejados: analisar projeções, covenants, vencimentos, orçamento, cenários de geração de caixa e eventos posteriores; avaliar se há incerteza relevante e se a divulgação é adequada. A leitura pública isolada não autoriza concluir sobre continuidade operacional. **Classificação:** R/P.

## PT 580 — Representações formais

Foi preparada minuta didática solicitando representações sobre responsabilidade pelas demonstrações, completude das informações, partes relacionadas, fraude, eventos subsequentes, litígios, estimativas e continuidade. A minuta não foi enviada e não substitui confirmação, inspeção, documento externo ou teste substantivo.

**Conclusão:** representação formal é evidência necessária em auditoria real, mas possui menor força isolada e deve ser corroborada. **Classificação:** P/S.

## PT 600 — Auditoria de grupos

O grupo deve ser mapeado por controladora, controladas, controladas em conjunto e investimentos relevantes. A documentação de 2025 menciona a participação da ENGIE na TAG e apresenta informações específicas da investida, inclusive equivalência patrimonial. Também devem ser considerados os componentes consolidados e as eliminações.

Procedimentos planejados: obter organograma e lista de componentes; definir materialidade de cada componente; avaliar competência e independência de auditores de componentes; instruir trabalhos; revisar achados; testar consolidação e eliminações. Não houve contato com auditores de componentes nem acesso a papéis de trabalho. **Classificação:** R/P.

## 5. Programas de auditoria por ciclo

### Receita

Obter composição da receita; reconciliar com DRE; testar cut-off; comparar contratos e faturamento; analisar notas de crédito; revisar transações incomuns; executar testes de lançamentos e investigar variações. Os procedimentos internos são planejados.

### Disponibilidades

Reconciliar saldos com balanço; examinar restrições; obter confirmações bancárias; testar conciliações; revisar aplicações e instrumentos financeiros. Confirmações não foram enviadas.

### Estoques

Confirmar relevância; observar contagem; testar cut-off; examinar custo e obsolescência; reconciliar inventário com razão. Inspeção física não foi realizada.

### Imobilizado

Reconciliar Nota 10 com razão; testar aquisições, baixas e transferências; examinar documentação; recalcular depreciação; testar vida útil e valor residual; avaliar impairment; realizar inspeção física planejada; usar a base sintética para testes de dados.

### Passivos

Pesquisar pagamentos posteriores; examinar fornecedores, dívida, concessões a pagar, provisões, tributos e benefícios; testar completude; ler contratos e covenants; circularizar advogados. Procedimentos internos são planejados.

### Estimativas

Identificar estimativas significativas; avaliar método, dados, premissas, incerteza e viés; recalcular; fazer sensibilidade; comparar estimativas anteriores com resultados posteriores. A aplicação à base sintética é didática.

## 6. Base sintética obrigatória

A base está em `base_imobilizado_engie/imobilizado_sintetico_500k.csv` e foi gerada por `gerar_base_imobilizado_engie.py`. Possui 500.000 linhas e 16 variáveis. Cada linha representa um bem sintético individual, mas não corresponde a registro real da ENGIE.

O total de `valor_contabil_liquido_mil` é R$ 28.567.889 mil, conciliado ao saldo consolidado de 31/12/2025. O arquivo `manifesto_geracao.json` registra a semente, a fonte e o hash SHA-256. O arquivo `erros_inseridos.csv` registra quatro exceções conhecidas. A base deve ser mantida separada das demonstrações reais.

## 7. Matriz de cobertura

| Norma | Papel | Cobertura |
|---|---|---|
| Estrutura Conceitual | PT EC | Objeto, critérios, asseguração e responsabilidades |
| NBC TA 200 | PT 200 | Ética, ceticismo, julgamento e risco |
| NBC TA 210 | PT 210 | Termos e precondições |
| NBC TA 220 | PT 220 | Qualidade, supervisão e consulta |
| NBC TA 230 | PT 230 | Documentação e referências |
| NBC TA 240 | PT 240 | Fraude e lançamentos |
| NBC TA 250 | PT 250 | Leis e regulamentos |
| NBC TA 260 | PT 260 | Comunicação com governança |
| NBC TA 265 | PT 265 | Deficiências de controle |
| NBC TA 300 | PT 300 | Estratégia e planejamento |
| NBC TA 315 | PT 315 | Riscos e entidade |
| NBC TA 320 | PT 320 | Materialidade |
| NBC TA 330 | PT 330 | Respostas aos riscos |
| NBC TA 402 | PT 402 | Serviços terceirizados |
| NBC TA 450 | PT 450 | Distorções |
| NBC TA 500 | PT 500 | Evidência |
| NBC TA 501 | PT 501 | Estoques, litígios e segmentos |
| NBC TA 505 | PT 505 | Confirmações |
| NBC TA 510 | PT 510 | Saldos iniciais |
| NBC TA 520 | PT 520 | Procedimentos analíticos |
| NBC TA 530 | PT 530 | Amostragem |
| NBC TA 540 | PT 540 | Estimativas |
| NBC TA 550 | PT 550 | Partes relacionadas |
| NBC TA 560 | PT 560 | Eventos subsequentes |
| NBC TA 570 | PT 570 | Continuidade |
| NBC TA 580 | PT 580 | Representações formais |
| NBC TA 600 | PT 600 | Grupos e componentes |

## 8. Conclusão integrada

A ENGIE Brasil Energia apresentou, em 31/12/2025, ativo consolidado de R$ 55.312.909 mil e imobilizado consolidado de R$ 28.567.889 mil. O imobilizado foi selecionado para a população sintética por sua magnitude e relação direta com a operação da companhia. A população possui 500.000 registros, foi gerada por código reproduzível e foi conciliada exatamente ao saldo contábil divulgado em R$ mil.

Os riscos mais relevantes concentram-se em existência, direitos, avaliação, depreciação, vida útil, impairment, contratos de concessão, receita, provisões, partes relacionadas, eventos subsequentes, continuidade e consolidação. A análise pública permitiu ler documentos, comparar saldos, calcular variações, mapear notas e avaliar divulgações. A base sintética permitiu executar testes de dados e amostragem didática, identificando quatro inconsistências intencionalmente inseridas.

Permanecem limitações materiais: não houve confirmação externa, entrevista, inspeção física, acesso a sistemas, exame de documentos internos, consulta a advogados, contato com a administração, contato com auditores ou revisão independente de terceiro. Portanto, este dossiê não contém opinião de auditoria nem conclusão profissional independente. As conclusões devem ser interpretadas como resultado de um estudo acadêmico baseado em evidências públicas e dados sintéticos.

## 9. Checklist antes da entrega

- [ ] Preencher matrícula, nome e data de preparação.
- [ ] Registrar a data de acesso de cada fonte.
- [ ] Conferir paginação no PDF baixado.
- [ ] Incluir o relatório do auditor e as notas usadas no repositório.
- [ ] Adicionar o script e os arquivos da base sintética.
- [ ] Verificar se a base possui 500.000 linhas.
- [ ] Verificar se a conciliação apresenta diferença zero.
- [ ] Manter o rótulo de dados sintéticos em todos os arquivos.
- [ ] Conferir a matriz de cobertura das normas.
- [ ] Gerar o PDF final e revisar referências cruzadas.
- [ ] Tornar o repositório acessível ao professor e testar o link em janela anônima.

## Referências

[1]: https://www.engie.com.br/wp-content/uploads/2026/02/DF-EBE-31.12.2025-vs_06_03-reap.pdf "ENGIE Brasil Energia — Relatório da Administração e Demonstrações Financeiras 2025 e 2024"

[2]: https://www.engie.com.br/wp-content/uploads/2025/01/Formulario-Cadastral-EBE-2025.pdf "ENGIE Brasil Energia — Formulário Cadastral 2025"

[3]: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp "CVM — Dados Abertos de DFP"

[4]: https://dados.cvm.gov.br/dataset/cia_aberta-doc-itr "CVM — Dados Abertos de ITR"

[5]: https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/17329/CODBOLSA/overview?language=pt-br "B3 — ENGIE Brasil Energia S.A."
