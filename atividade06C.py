# Peça ao usuário que diga quantas notas quer digitar e em seguida, faça a media.

print('### NOTAS ###')

quantidade = int(input('Quantas notas você deseja digitar? '))

i = 1
boletim = []

while (i <= quantidade):
    print('Valor da {}ª nota.' . format(i))
    notas = float(input('Digite o valor da nota: '))
    i += 1
    boletim.append(notas)

soma = 0

for nota in boletim:
    soma = soma + nota
    print(soma)

media = (soma) / quantidade
print('A média é: {}.' . format(media))