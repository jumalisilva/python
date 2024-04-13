# Faça um algoritmo que, dados três números inteiros representando dia, mês e ano de uma data, imprima qual o dia seguinte.

print('Digite uma data e descubra o dia seguinte dela!')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o número do mês: '))
ano = int(input('Digite o ano: '))

# Fevereiro
if (mes == 2 and dia < 28):
    dia += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))
elif (mes == 2 and dia > 28):
    print('O mês {} possui apenas 28 dias. Tente novamente.' . format(mes))
elif (mes == 2 and dia == 28):
    dia -= 27
    mes += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))

# Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia < 30:
    dia += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print('O mês {} possui apenas 30 dias. Tente novamente.' . format(mes))
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 30:
    dia -= 29
    mes += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))

# Meses com 31 dias
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia < 31:
    dia += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia > 31:
    print('O mês {} possui apenas 31 dias. Tente novamente.' . format(mes))
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia == 31:
    dia -= 30
    mes += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))

# Dezembro (31 dias)
elif (mes == 12) and dia < 31:
    dia += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))
elif (mes == 12) and dia > 31:
    print('O mês {} possui apenas 31 dias. Tente novamente.' . format(mes))
elif (mes == 12) and dia == 31:
    dia -= 30
    mes -= 11
    ano += 1
    print('A data seguinte é: {}/{}/{}.' . format(dia, mes, ano))