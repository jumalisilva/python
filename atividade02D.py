# D) Escreva um programa que simula o jogo de um(a) jogador(a) contra o(a) outro(a).

print('Bem-vindo ao jogo da Pedra, Papel e Tesoura!')

jogador1 = input('Jogador 1, escolha entre pedra, papel ou tesoura: ')
jogador2 = input('Jogador 2, escolha entre pedra, papel ou tesoura: ')

# Pedra e tesoura
if (jogador1 == 'pedra' and jogador2 == 'tesoura'):
    print('Jogador 1 venceu!')
elif (jogador2 == 'pedra' and jogador1 == 'tesoura'):
    print('Jogador 2 venceu!')
    
# Tesoura e papel
elif (jogador1 == 'tesoura' and jogador2 == 'papel'):
    print('Jogador 1 venceu!')
elif (jogador2 == 'tesoura' and jogador1 == 'papel'):
    print('Jogador 2 venceu!')

# Papel e pedra
elif (jogador1 == 'papel' and jogador2 == 'pedra'):
    print('Jogador 1 venceu!')
elif (jogador2 == 'papel' and jogador1 == 'pedra'):
    print('Jogador 2 venceu!')

# Empate
elif (jogador1 == jogador2):
    print('Empate!')