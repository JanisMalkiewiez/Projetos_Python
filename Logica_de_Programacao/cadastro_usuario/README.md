# 📝 Prática de Python: Manipulação de Strings e Validação de Dados

Este projeto contém exercícios e práticas focados em manipulação de strings, listas e limpeza de dados (sanitização) em Python. O objetivo principal foi simular o recebimento e tratamento de dados de formulários web (como os utilizados em frameworks como o Django) e prepará-los para armazenamento no banco de dados.

## 🚀 O que foi praticado

Neste repositório, explorei os seguintes conceitos e ferramentas da linguagem Python:

* **Limpeza e Formatação de Strings:** 
  * Uso de `.strip()`, `.lower()` e `.title()` para sanitização e padronização de entradas (ex: e-mails minúsculos e nomes capitalizados).
  * Uso de `.replace()` para remoção de caracteres de máscara (ex: retirar pontos e traços de CPFs e Celulares).
* **Contagem e Validação:** 
  * Uso da função *built-in* `len()` para verificar a quantidade exata de caracteres.
* **Controle de Fluxo e Operadores:** 
  * Estruturas condicionais `if` e `else` para aplicar as regras de negócio de validação.
  * Operador de associação `in` para verificar múltiplos cenários válidos de forma enxuta (ex: `len(celular) in (10, 11)`).

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
