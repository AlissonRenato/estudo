palavra1 = "Brasil hexa 2026"
palavra2 = "Brasil! hexa 2026!"
len(palavra1)
len(palavra2)
print(f'Brasil hexa 2026: {len(palavra1)} caracteres\nBrasil! hexa 2026!: {len(palavra2)}caracteres')
if len(palavra1) != len(palavra2):
    print("As strings possuem tamanhos diferentes!")
else:
    print("O tamanho das strings são iguais!") 