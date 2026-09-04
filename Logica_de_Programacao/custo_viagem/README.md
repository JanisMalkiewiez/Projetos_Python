# 🗺️ Simulador de Custos de Viagem 🚗💸

> Um roteirizador financeiro inteligente desenvolvido em Python para você planejar suas viagens de carro sem surpresas no bolso!

Vai pegar a estrada no fim de semana ou planejar uma rota de entregas? Este script cruza a distância do trajeto com a eficiência do seu veículo e o preço atual do combustível na bomba, entregando um relatório completo de quanto você vai gastar para chegar ao seu destino.

---

### ✨ O que o programa faz?
- 🛣️ Solicita a distância total do trajeto planejado (em km).
- ⚙️ Recebe a média de consumo do seu carro (quantos km ele faz por litro).
- ⛽ Pede o preço atualizado do combustível.
- 🧮 Calcula com precisão quantos litros serão necessários para completar a viagem e o valor total que será gasto.
- 🧾 Formata o relatório final como um cupom limpo, arredondando as métricas para duas casas decimais.
- 🚦 Avalia o impacto financeiro da rota e classifica a viagem em:
  - **Viagem econômica** 🟢 (Abaixo de R$ 100)
  - **Custo moderado** 🟡 (Até R$ 300)
  - **Viagem cara** 🔴 (Acima de R$ 300)

---

### 🛠️ Conceitos praticados
Neste projeto, elevamos a complexidade unindo múltiplas variáveis e realizando cálculos em cadeia:

- **Entrada de Múltiplos Dados:** Coleta de três informações distintas do usuário em sequência usando `input()`.
- **Conversão de Tipos (Casting):** Transformação das entradas em números decimais com `float()` para suportar distâncias e preços quebrados (ex: R$ 5.89).
- **Cálculos Sequenciais:** Uso do resultado da primeira operação de divisão (`distancia / consumo`) como base para a segunda operação de multiplicação (`litros_necessarios * preco_combustivel`).
- **Formatação de Dados:** Utilização massiva da função `round(variavel, 2)` combinada com a conversão para texto via `str()` nas saídas finais.
- **Estruturas Condicionais Aninhadas:** Blocos `if`, `elif` e `else` aplicados para classificar o custo final em faixas de orçamento.