# Criar um algoritmo que dê a opção do usuário escolher se deseja calcular a área de um triângulo, quadrado ou círculo. 
# Você deve perguntar a ele os valores e em seguida exibir o resultado.

escolha = input('Escolha uma figura para calcular a área: quadrado, triângulo ou círculo. ')

if (escolha == 'quadrado'):
    lado1 = float(input('Digite o valor do primeiro lado: '))
    lado2 = float(input('Digite o valor do segundo lado: '))
    quadrado = lado1 * lado2
    print('A área do quadrado é: {}' . format(quadrado))
elif (escolha == 'triângulo'):
    base = float(input('Digite o valor da base: '))
    altura = float(input('Digite o valor da altura: '))
    triangulo = (base * altura) / 2
    print('A área do triângulo é: {}' . format(triangulo))
elif (escolha == 'círculo'):
    raio = float(input('Digite o valor do raio: '))
    circulo = 3.14 * (raio ** 2)
    print('A área do círculo é: {}' . format(circulo))