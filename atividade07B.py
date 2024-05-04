# Crie uma calculadora simples que permita ao usuário realizar operações básicas de adição, subtração, multiplicação e divisão.

def calculadora ():
    a = float(input('Escolha o primeiro número: '))
    b = float(input('Escolha o segundo número: '))
    operacao = input('Agora escolha uma operação:\n Soma \n Subtração \n Multiplicação \n Divisão \n Digite sua escolha: ')
    soma = a + b
    sub = a - b
    multi = a * b
    div =  a / b

    if (operacao == 'soma'):
        print('A soma de {} com {} é: {}.' . format(a, b, soma))
    elif (operacao == 'subtração'):
        print('A subtração de {} com {} é: {}.' . format(a, b, sub))
    elif (operacao == 'multiplicação'):
        print('A multiplicação de {} com {} é: {}.' . format(a, b, multi))
    elif (operacao == 'divisão'):
        print('A divisão de {} com {} é: {}.' . format(a, b, div))
    
calculadora()