# 🌡️ Conversor de Temperatura & Termômetro Smart ☀️❄️

> Um utilitário rápido desenvolvido em Python para converter temperaturas de Celsius para Fahrenheit e analisar o clima instantaneamente!

Seja para planejar uma viagem internacional onde o sistema de medidas é diferente, ou apenas para praticar a famosa fórmula de conversão física, este programa faz o cálculo em milissegundos e ainda te avisa se é melhor pegar um casaco ou roupas leves.

---

### ✨ O que o programa faz?
- 🌡️ Recebe a temperatura atual informada pelo usuário em graus Celsius.
- 🧮 Aplica a fórmula matemática padrão de conversão `(C × 9/5) + 32` para encontrar o valor correspondente em Fahrenheit.
- 📺 Exibe o resultado exato na tela de forma amigável.
- 🌤️ Atua como um "termômetro inteligente", avaliando o valor em Celsius e classificando o clima como:
  - **Frio** (abaixo de 15°C) 🥶
  - **Temperatura agradável** (entre 15°C e 30°C) 😎
  - **Quente** (acima de 30°C) 🥵

---

### 🛠️ Conceitos praticados
Este projeto é um excelente exercício prático de lógica de programação e matemática. Os conceitos aplicados foram:

- **Entrada e Saída de dados:** Interação com o usuário via `input()` e respostas com `print()`.
- **Fórmulas Matemáticas:** Tradução de uma fórmula algébrica real para a sintaxe do Python usando operadores de multiplicação (`*`), divisão (`/`) e adição (`+`).
- **Conversão de Tipos (Casting):** Uso de `float()` para aceitar números decimais na entrada e `str()` para concatenar o resultado numérico com o texto final.
- **Estruturas Condicionais Aninhadas:** Avaliação de múltiplos cenários utilizando `if`, `elif` e `else` para definir a sensação térmica.