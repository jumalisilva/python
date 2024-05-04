# Crie um código que pergunte a uma pessoa se ela tem habilitação e se o documento do veículo está em dia. Caso contrário, o programa deve exibir "veículo apreendido".

def habilitacao ():
    pergunta = input('Você tem habilitação? (S/N) ')
    documento = input('A documentação do veículo está em dia? (S/N) ')

    if (pergunta == 'S' and documento == 'S'):
        print('Veículo liberado!')
    elif (pergunta == 'S' and documento == 'N'):
        print('Veículo apreendido.')
    else:
        print('Veículo apreendido.')

habilitacao()