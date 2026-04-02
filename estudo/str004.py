nome = input("Seu nome:")
sexo = input("Seu sexo:")
idade = int(input("Sua idade:"))
if sexo == "feminino" and idade < 25:
    print(nome)
    print("ACEITO")
else:
    print("NÃO ACEITO")
