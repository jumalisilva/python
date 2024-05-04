# Crie um código que pergunte a uma pessoa se ela tem habilitação e se o documento do veículo está em dia. Caso contrário, o programa deve exibir "veículo apreendido".
pergunta = input('Você tem habilitação? (S/N) ')
documento = input('A documentação do veículo está em dia? (S/N) ')

def habilitacao (pergunta, documento): # parâmetro
    if (pergunta == 'S' and documento == 'S'):
        print('Veículo liberado!')
    else:
        print('Veículo apreendido.')

habilitacao(pergunta, documento) # variável