# Ler uma frase e contar quantas vezes cada palavra aparece.
frase = input("Digite qualquer frase:").split()
dicionario = {}
for palavra in frase :
    if palavra in dicionario :
        dicionario[palavra] += 1
    else :
        dicionario[palavra] = 1
print(dicionario)