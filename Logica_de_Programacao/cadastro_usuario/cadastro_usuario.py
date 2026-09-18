print("--- CADASTRO DE USUÁRIO ---")

nome = input("Nome: ").strip().title()
email = input("Email: ").strip().lower()
celular = input("Celular: ").strip().replace("-", "").replace(" ", "")
cpf = input("Digite o CPF (ex: 111.222.333-44): ").strip().replace(".", "").replace("-", "")

print("\nDados coletados e tratados com sucesso na memória!")

print("--- RESUMO DOS DADOS TRATADOS ---")
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Celular: {celular}")
print(f"CPF: {cpf}")

print("--- VALIDAÇÃO DE DADOS ---")

if len(cpf) == 11:
    print("✅ CPF com quantidade correta de dígitos.")
else:
    print("❌ CPF inválido.")

if len(celular) in (10, 11):
    print("✅ Celular com tamanho válido.")
else:
    print("❌ Celular inválido.")