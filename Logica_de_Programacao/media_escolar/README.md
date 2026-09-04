# 🎓 Sistema de Boletim Escolar & Média 📚

> Um programa direto ao ponto desenvolvido em Python para calcular médias de notas e automatizar o resultado acadêmico de forma simples e rápida!

Ideal para professores que precisam fechar notas, estudantes acompanhando seu próprio desempenho durante o semestre ou como um ótimo exercício prático de lógica escolar. O script faz a matemática e já entrega a situação do aluno mastigada.

---

### ✨ O que o programa faz?
- 📝 Solicita a inserção de 3 notas de avaliações (podem ser números inteiros ou decimais).
- 🧮 Calcula a média aritmética somando as notas e dividindo pela quantidade de provas.
- 🎯 Arredonda o resultado final para duas casas decimais, garantindo um "boletim" limpo e exato.
- 🚦 Analisa o desempenho e classifica o aluno automaticamente nas seguintes situações:
  - **Aprovado** 🟢 (Média igual ou superior a 10)
  - **Recuperação** 🟡 (Média entre 5 e 9.99)
  - **Reprovado** 🔴 (Média abaixo de 5)

---

### 🛠️ Conceitos praticados
Neste projeto, trabalhamos fortemente com a ordem de precedência matemática e a validação de regras de negócio, utilizando:

- **Entrada e Saída de dados:** Interatividade com `input()` e respostas concatenadas com `print()`.
- **Conversão de Tipos (Casting):** Uso de `float()` para aceitar notas com casas decimais (ex: 8.5) e `str()` na saída.
- **Precedência de Operadores:** Uso de parênteses `( )` para garantir que a soma das notas seja executada *antes* da divisão por 3.
- **Arredondamento:** Uso da função `round(variavel, 2)` para reatribuir o valor da variável de forma formatada.
- **Estruturas Condicionais Aninhadas:** Blocos lógicos `if`, `elif` e `else` para criar as regras de aprovação escolar.