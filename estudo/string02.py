# Crie um programa que compara duas strings lidas pelo usuário (perguntar os nomes)
nome1 = input("Digite um nome:")
nome2 = input("Digite um nome:")
nome1.lower().strip()
nome2.lower().strip()
if nome1.lower().strip() == nome2.lower().strip():
    print("São iguais")
else:
    print("Não são")
