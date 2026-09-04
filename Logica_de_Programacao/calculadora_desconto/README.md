# 🏷️ Calculadora de Descontos Smart 💸

> Uma ferramenta ágil desenvolvida em Python para calcular o valor exato de promoções e gerenciar a precificação de produtos de forma eficiente.

Seja para ajustar os preços de um catálogo de vendas online, planejar ofertas para clientes ou apenas conferir o valor real daquele item na promoção, este script resolve a matemática em segundos! Ele ainda categoriza automaticamente se o preço final do produto está na faixa de "baixo custo" ou não.

---

### ✨ O que o programa faz?
- 💰 Recebe o preço original de qualquer produto.
- 📉 Calcula o desconto desejado de forma inteligente (o usuário pode digitar `20` ou `20%`, e o código entende e limpa o símbolo automaticamente!).
- 🧾 Exibe de forma clara e arredondada o valor exato que foi descontado e o preço final a pagar.
- 📊 Analisa o resultado final e classifica o produto automaticamente como "preço baixo" (abaixo de 
R$ 50) ou "preço normal".

---

### 🛠️ Conceitos praticados
Neste projeto, o código foi otimizado para lidar com dados de entrada de forma mais robusta, aplicando:

- **Entrada e Saída de dados:** Interatividade com `input()` e concatenação em `print()`
- **Manipulação de Strings:** Uso do método `.replace()` para higienizar os dados digitados pelo usuário, removendo caracteres indesejados como o `%`.
- **Conversão de Tipos:** Transformação de textos para números decimais com `float()`.
- **Operações Matemáticas:** Cálculo de porcentagem e subtração de valores.
- **Arredondamento:** Formatação de moedas utilizando a função `round(variavel, 2)` para limitar as casas decimais.
- **Estruturas Condicionais:** Lógica de negócio aplicada com `if` e `else` para classificar a faixa de preço do produto.