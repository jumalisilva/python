# Faça um programa que leia 5 notas e armazene em uma lista.

print('### NOTAS ###')
i = 1
boletim = []

while (i <= 5):
    print('Valor da {}ª nota.' . format(i))
    notas = float(input('Digite o valor da nota: '))
    i += 1
    boletim.append(notas)

for nota in boletim:
    print(nota)