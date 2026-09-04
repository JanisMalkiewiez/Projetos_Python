# 💼 Analisador de Salário Líquido 💵

> Um script prático e direto desenvolvido em Python para calcular ganhos reais e categorizar faixas salariais em segundos.

Ideal para gestão financeira pessoal, simulações de folha de pagamento ou para testar lógicas de negócios, este programa automatiza o cálculo do salário líquido e já entrega uma análise básica de qual faixa de renda o valor se encaixa.

---

### ✨ O que o programa faz?
- 💰 Recebe o valor do salário bruto e o total de descontos aplicados.
- 🧮 Processa a subtração matemática para encontrar o valor líquido exato.
- 🧾 Formata a saída de texto para o padrão de moeda, garantindo a exibição de apenas duas casas decimais.
- 📊 Analisa o resultado final e classifica automaticamente o salário em três categorias: 
  - **Baixo** (menor que R$ 1.500)
  - **Médio** (entre R$ 1.500 e R$ 3.000)
  - **Alto** (acima de R$ 3.000)

---

### 🛠️ Conceitos praticados
Neste projeto, avançamos na estruturação de múltiplas condições lógicas, aplicando os seguintes fundamentos:

- **Entrada e Saída de dados:** Uso do `input()` para captar os valores e concatenação com `print()`.
- **Conversão de Tipos (Casting):** Transformação das entradas em números decimais com `float()` e conversão de volta para texto com `str()` na hora de exibir.
- **Operações Matemáticas Básicas:** Subtração de variáveis (`salario_bruto - descontos`).
- **Arredondamento:** Limitação das casas decimais utilizando a função `round(variavel, 2)`.
- **Estruturas Condicionais Aninhadas:** Uso de blocos `if`, `elif` e `else` para criar diferentes caminhos de execução baseados em múltiplos intervalos de valores.