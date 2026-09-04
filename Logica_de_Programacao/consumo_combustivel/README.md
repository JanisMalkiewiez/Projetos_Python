# 🚗 Calculadora de Consumo de Combustível ⛽

> Um script prático e eficiente desenvolvido em Python para descobrir a média de consumo do seu veículo e ajudar no controle de gastos!

Seja para planejar uma viagem de carro, dividir a gasolina com os amigos ou apenas descobrir se o seu veículo está "bebendo" demais, brincadeiras a parte. Este programa faz o cálculo rápido de quilômetros por litro (km/l) e avalia a eficiência do motor.

---

### ✨ O que o programa faz?
- 🛣️ Recebe a distância total percorrida na viagem (em km).
- ⛽ Pede a quantidade de combustível consumida (em litros).
- 🧮 Calcula a média exata de consumo do veículo (km/l).
- 🧾 Formata o resultado para exibir apenas duas casas decimais, deixando a leitura mais limpa.
- 🚦 Avalia o desempenho do veículo e classifica o consumo em:
  - **Alto!** 🔴 (Menos de 8 km/l)
  - **Médio!** 🟡 (Entre 8 e 12 km/l)
  - **Baixo!** 🟢 (Mais de 12 km/l - muito econômico!)

---

### 🛠️ Conceitos praticados
Neste projeto, reforçamos a lógica matemática aplicada a situações do dia a dia, utilizando os seguintes conceitos:

- **Entrada e Saída de dados:** Coleta de informações com `input()` e exibição com `print()`.
- **Conversão de Tipos (Casting):** Uso de `float()` para aceitar números decimais (como metragens quebradas) e `str()` para exibir o resultado junto ao texto.
- **Operações Matemáticas:** Uso do operador de divisão (`/`) para encontrar a proporção entre distância e litros.
- **Arredondamento:** Uso da função `round(variavel, 2)` para limitar a quantidade de casas decimais.
- **Estruturas Condicionais Aninhadas:** Avaliação do resultado utilizando `if`, `elif` e `else` para classificar a eficiência do veículo.