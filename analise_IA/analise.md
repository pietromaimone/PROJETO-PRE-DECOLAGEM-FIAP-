# 1.5 Análise Assistida por IA — Sistema de Pré-Decolagem

Relatório analítico gerado a partir do processamento dos 100 cenários de telemetria contidos no arquivo `banco_de_dados_real.csv`.

---

## 1. Classificação dos Dados

A base de dados avaliada contém **100 cenários** estruturados em **14 variáveis**, categorizadas em três eixos principais:

### A. Parâmetros Físicos e Ambientais
* **`temperatura_interna`**: Varia de 0,0 °C a 49,0 °C (Média: 24,89 °C; Envelope de segurança: 18 °C a 35 °C).
* **`temperatura_externa`**: Varia de -136,0 °C a 60,0 °C (Média: 23,49 °C; Faixa admissível: -120 °C a 50 °C).
* **`pressao_dos_tanques`**: Varia de 20,0 a 50,0 psi (Média: 35,52 psi; Intervalo seguro: 30 a 40 psi).
* **`integridade_estrutural`**: Indicador binário (1 = Íntegro, 0 = Comprometido; 54% de conformidade).

### B. Subsistemas Críticos e Aviônica
* **`status_navegacao`**: Binário (52% operacional).
* **`status_comunicacao`**: Binário (57% operacional).
* **`status_propulsao`**: Binário (47% operacional).
* **`status_lifesuport`**: Binário (50% operacional).

### C. Parâmetros de Balanço Energético
* **`capacidade_total_kwh`**: Varia de 506 a 1.998 kWh (Média: 1.333,61 kWh).
* **`nivel_de_energia`**: Varia de 0,0% a 99,0% (Média: 51,44%; Requisito mínimo de decolagem: 70%).
* **`consumo_decolagem_kwh`**: Varia de 50 a 199 kWh (Média: 120,68 kWh).
* **`perdas_kwh`**: Varia de 5 a 50 kWh (Média: 25,59 kWh).

### D. Classificação Global de Decolagem
* **Prontos para Decolar (GO):** **7 cenários** (`cenario_2`, `cenario_16`, `cenario_36`, `cenario_51`, `cenario_83`, `cenario_93`, `cenario_100`).
* **Decolagens Abortadas (NO-GO):** **93 cenários**.
* **Acurácia do Algoritmo vs. Gabarito:** **100/100 (100% de precisão)**.

---

## 2. Identificação de Possíveis Anomalias

A inspeção estatística identificou anomalias críticas que explicam a taxa de 93% de aborto:

1. **Déficit Energético Generalizado (69% de incidência):**
   * Em 69 cenários o nível de carga da bateria estava abaixo de 70%, registrando-se leituras extremas anômalas de **0%** de carga reportada.
2. **Despressurização e Sobrepressão nos Tanques (60% de incidência):**
   * Foram detectados extremos de **20 psi** (pressão perigosamente insuficiente para alimentação das bombas) e **50 psi** (risco iminente de ruptura estrutural de linhas de combustível).
3. **Extremos Térmicos Críticos:**
   * A temperatura interna violou a margem segura em **58 cenários**, registrando leituras mínimas de até **0 °C** (risco para tripulação e congelamento de fluidos de bordo).
   * A temperatura externa chegou a **-136 °C** (ultrapassando o piso criogênico de -120 °C) e picos de **+60 °C** (superando o limite térmico de absorção radiativa de 50 °C).
4. **Degradação Concomitante de Subsistemas Críticos:**
   * Falhas simultâneas de propulsão (53%) e suporte de vida (50%) ocorreram com frequência atípica, indicando vulnerabilidade a falhas em cascata ou pane em barramentos compartilhados.

---

## 3. Sugestões de Risco e Medidas Mitigatórias

| Nível de Risco | Área Crítica | Descrição do Risco Operacional | Ação Mitigadora Recomendada |
| :--- | :--- | :--- | :--- |
| **Crítico** | Propulsão e Suporte de Vida | Taxa de indisponibilidade de ~50% nos módulos primários inviabiliza missões com segurança. | Projetar redundância ativa com barramentos elétricos independentes e isolamento galvânico entre aviônica e propulsão. |
| **Crítico** | Pressurização de Tanques | Variação de 20 a 50 psi pode levar a cavitação nas turbobombas ou ruptura mecânica por sobrepressão. | Instalar válvulas reguladoras pneumáticas com alívio duplo e sistema de pressurização autocompensada por gás inerte (Hélio). |
| **Alto** | Reserva Energética Pós-Decolagem | Cenários autorizados operam próximos do limiar (ex.: `cenario_93` com apenas 356 kWh restantes). | Estabelecer critério de corte adicional: além dos 70% iniciais, exigir reserva técnica mínima fixa ($\ge 500\text{ kWh}$) pós-decolagem. |
| **Alto** | Condicionamento Térmico Interno | Leituras de 0 °C no interior da cabine inviabilizam tripulação e degradam a química das baterias. | Implementar ciclo de pré-aquecimento assistido por solo acoplado à torre de serviço até T-30s. |
| **Médio** | Telemetria de Carga da Bateria | Leituras de 0% de energia apontam potencial problema nos sensores de estado de carga (SoC). | Integrar validação cruzada por hardware entre medição de tensão em circuito aberto (OCV) e contagem de coulombs. |

---

## 4. Detalhamento Energético dos Cenários Liberados

| Cenário ID | Capacidade Total | Carga Inicial | Consumo Decolagem | Perdas | Energia Restante | Autonomia Pós-Voo |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `cenario_2` | 1.063 kWh | 70,0% | 100 kWh | 31 kWh | 613,10 kWh | **57,68%** |
| `cenario_16` | 1.994 kWh | 97,0% | 157 kWh | 49 kWh | 1.728,18 kWh | **86,67%** |
| `cenario_36` | 1.144 kWh | 93,0% | 134 kWh | 16 kWh | 913,92 kWh | **79,89%** |
| `cenario_51` | 1.196 kWh | 71,0% | 79 kWh | 22 kWh | 748,16 kWh | **62,56%** |
| `cenario_83` | 693 kWh | 83,0% | 105 kWh | 16 kWh | 454,19 kWh | **65,54%** |
| `cenario_93` | 603 kWh | 91,0% | 170 kWh | 23 kWh | 355,73 kWh | **58,99%** |
| `cenario_100` | 1.996 kWh | 99,0% | 200 kWh | 39 kWh | 1.737,04 kWh | **87,03%** |