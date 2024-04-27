# Com o programa anterior (atividade06A), calcule a média das notas digitadas.

print('### NOTAS ###')
i = 1
boletim = []

while (i <= 5):
    print('Valor da {}ª nota.' . format(i))
    notas = float(input('Digite o valor da nota: '))
    i += 1
    boletim.append(notas)

soma = 0

for nota in boletim:
    soma = soma + nota
    print(soma)

media = (soma) / 5
print('A média é: {}.' . format(media))