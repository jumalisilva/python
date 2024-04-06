# A) Crie um algoritmo que receba um número e retorne "positivo" se o número for maior que zero, "negativo" se for menor que zero.

num = float(input('Digite um número: '))

if (num > 0):
    print('{} é positivo.' . format(num))
elif (num == 0):
    print('{} é neutro.' . format(num))
else:
    print('{} é negativo.' . format(num))