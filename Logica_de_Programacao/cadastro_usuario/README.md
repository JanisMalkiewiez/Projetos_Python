# 📝 Prática de Python: Manipulação de Strings e Validação de Dados

Este projeto contém exercícios e práticas focados em manipulação de strings, listas e limpeza de dados (sanitização) em Python. O objetivo principal foi simular o recebimento e tratamento de dados de formulários web (como os utilizados em frameworks como o Django) e prepará-los para armazenamento no banco de dados.

## 🚀 O que foi praticado

Neste repositório, explorei os seguintes conceitos e ferramentas da linguagem Python:

* **Fatiamento (Slicing):** Inversão de strings utilizando o passo negativo `[::-1]`.
* **Métodos de Strings:** 
  * `.count()` e `.find()` para buscar e contar ocorrências de caracteres e palavras.
  * `.strip()`, `.lower()` e `.title()` para limpeza e padronização (ex: nomes e e-mails).
  * `.replace()` para remoção de formatações indesejadas (ex: pontos e traços em CPFs e Celulares).
  * `.split()` e `.join()` para conversão entre strings e listas.
* **Operações com Listas:** Acesso a itens por índices (`[0]`, `[-1]`) e contagem total de elementos utilizando `len()`.
* **Estruturas Condicionais e Operadores:** Uso do `if` junto com o operador de associação `in` para validações de regras de negócio (ex: verificar se o tamanho do celular é válido).

## 📂 Estrutura do Projeto

Para demonstrar boas práticas de desenvolvimento e documentação, o projeto foi dividido em dois formatos:

* **`demonstracao_cadastro.ipynb` (Jupyter Notebook):** Arquivo focado em apresentação. Contém o passo a passo da lógica dividida em blocos (células), intercalando explicações em Markdown com o código e mostrando visualmente o resultado final das validações.
* **`sistema_cadastro.py` (Script Python):** Arquivo limpo com o código completo, pronto para ser executado via terminal, demonstrando como o script rodaria em um ambiente de produção.

## 💻 Como executar o Script localmente

Se desejar testar o código no seu próprio terminal, siga os passos abaixo:

1. Clone o repositório ou baixe os arquivos.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute o comando:
   ```bash
   python sistema_cadastro.py