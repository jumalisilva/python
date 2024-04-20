# Faça um programa que solicite um número e imprima a tabuada desse número até 10

num = int(input('Digite um número para descobrir sua tabuada: '))
i = 0

while (i <= 10):
    res = num * i
    print('{} x {} = {}' . format(num, i, res))
    i += 1