# 🚀 Pra Decolagem

Projeto de simulação de verificação pré-lançamento de uma espaçonave, integrando **telemetria**, **algoritmos de decisão**, **análise energética** e **inteligência artificial** para determinar se as condições são seguras para decolagem.

## 📋 Sobre o projeto

O sistema simula a leitura de dados de sensores de uma nave espacial e, a partir de faixas de segurança predefinidas, decide automaticamente entre:

- ✅ **PRONTO PARA DECOLAR**
- ❌ **DECOLAGEM ABORTADA**

Além da lógica de decisão, o projeto inclui uma análise da autonomia energética da nave e uma etapa de análise assistida por IA para classificação de dados e identificação de anomalias.

## 🗂️ Estrutura do projeto

### 1.1 Organização e descrição da telemetria
Interpretação dos dados recebidos dos sensores da nave:
- Temperatura interna e externa
- Integridade estrutural (0/1)
- Níveis de energia (%)
- Pressão dos tanques
- Status dos módulos críticos

### 1.2 Algoritmo de verificação
Fluxograma/pseudocódigo que define a lógica de decisão entre **PRONTO PARA DECOLAR** e **DECOLAGEM ABORTADA**, com base em faixas seguras predefinidas para cada variável de telemetria.

### 1.3 Script em Python
Implementação da lógica do algoritmo em Python, simulando:
- Leitura dos dados de telemetria
- Execução das verificações de segurança
- Impressão do resultado final

### 1.4 Análise energética
Cálculo da autonomia inicial da nave, considerando:
- Capacidade total (kWh)
- Carga atual (%)
- Consumo estimado na decolagem
- Perdas energéticas

### 1.5 Análise assistida por IA
Uso de IA para apoiar a tomada de decisão, incluindo:
- Classificação dos dados de telemetria
- Identificação de possíveis anomalias
- Sugestões de nível de risco

### 1.6 Reflexão crítica
Texto de reflexão abordando:
- Ética e responsabilidade
- Impacto social da exploração espacial
- Sustentabilidade tecnológica

## 🛠️ Tecnologias utilizadas

- **Python** — implementação do algoritmo de verificação e simulação
- **IA** — apoio à análise de dados e identificação de riscos

## ▶️ Como executar

```bash
python main.py
```

> Ajuste o nome do arquivo/comando acima conforme a estrutura real do seu script.

## 📊 Exemplo de saída esperada

```
Verificando telemetria...
Temperatura interna: OK
Temperatura externa: OK
Integridade estrutural: OK
Nível de energia: OK
Pressão dos tanques: OK
Status dos módulos: OK

>>> PRONTO PARA DECOLAR ✅
```

## 📄 Licença

Projeto acadêmico/educacional — livre para estudo e adaptação.
