# Descobrir se um número inteiro fornecido pelo usuário é primo.
n = int(input("Informe o numero: "))

if n <= 1:
    print("Não é primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Não é primo")
            break
    else:
        # Este else pertence ao FOR, não ao IF. 
        # Ele só roda se o break NUNCA foi acionado.
        print("É primo")