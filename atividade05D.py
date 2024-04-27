# Crie um jogo em que o jogador tenta adivinhar um número. O programa deve fornecer dicas se o palpite do jogador for muito alto ou muito baixo.

numeroAleatorio = int(input('Digite um número: '))
numeroCorreto = 17


while numeroAleatorio != numeroCorreto:
    if (numeroAleatorio < numeroCorreto):
        print('Quase lá, tente novamente!')
        numeroAleatorio = int(input('Digite um número: '))
    elif (numeroAleatorio > numeroCorreto):
        print('Ops, passou um pouco. Tente novamente.')
        numeroAleatorio = int(input('Digite um número: '))

print('Parabéns, você acertou o número aleatório!')    