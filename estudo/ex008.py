# Faça um programa que decida se duas strings
# lidas do teclado são palíndromas mútuas, ou
# seja, se uma é igual à outra quando lida de traz
# para frente.
# ▪ Exemplo: amor e roma.
nome_1 = input("Digite um nome:")
nome_2 = input("Digite outro nome:")
nome_1[::-1]
nome_2[::-1]
if nome_1 == nome_2[::-1]:
    print("São palíndromas mútuas!")
else:
    print("Não são palíndromas mútuas")    