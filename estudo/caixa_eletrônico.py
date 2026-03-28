# Simular um saque onde o programa diz quantas notas de cada valor serão entregues (notas de 50, 20, 10 e 1).
valor = int(input("Informe o valor do saque :"))
total_cedulas = 0
while valor >=50:
    valor-=50
    total_cedulas +=1
if total_cedulas > 0 :
    print(f"O total de cedulas de 50 são :{total_cedulas}")
total_cedulas = 0
while valor >= 20:
    valor -= 20
    total_cedulas+= 1
if total_cedulas > 0:
    print(f"O total de cedulas de 20 são: {total_cedulas}")
total_cedulas = 0
while valor >=10:
    valor-= 10
    total_cedulas+=1
if total_cedulas > 0:
    print(f"O total de cedulas de 10 são: {total_cedulas}")
total_cedulas = 0
while valor >= 1:
    valor-=1
    total_cedulas+=1
if total_cedulas > 0:
    print(f"O total de cedulas de 1 real são {total_cedulas} ")
total_cedulas = 0
while valor == 0:
    break
# Um dos maiores aprendizados desse exercicio  é fixar que o progrma lê meu código de cima para baixo, o que parece e é obvio !
# Mas é interessante pq eu entendo que não posso colocar a condição no while junto com o print, senão ele printa um monte de vezes.
