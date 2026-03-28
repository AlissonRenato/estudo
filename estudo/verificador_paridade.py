# Criar um programa que peça um número ao usuário e diga se ele é Par ou Ímpar.
cont = 0
while cont < 5:
    cont+=1
    num = int(input("Informe o numero :"))
    if num % 2 == 0 :
        print("é par")
    else :
        print("é impar")


    