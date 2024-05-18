# Criando uma função que retorna se um número é positivo ou negativo

def positivoOuNegativo(numero):
    if numero > 0:
        return '{} é positivo' . format(numero)
    elif numero < 0:
        return '{} é negativo' . format(numero)
    else:
        return '{} é neutro' . format(numero)
    
# print(positivoOuNegativo(-5))
# print(positivoOuNegativo(50))
# print(positivoOuNegativo(0))
    
# ___________________________________ // _____________________________________
    
# Variáveis globais (todas as funções têm acesso) e locais (somente a função na qual ela é criada tem acesso)
    
val1 = 0 # variável global

def soma():
    a = 0 # variável local
    return val1 + a

# tratamento e excessão -> págs 40 e 41 da apostila
def div(b):
    try: # o try significa "tentar", ou seja, ele tenta executar sempre o caso abaixo
        return val1 / b # variável parâmetro com escopo local
    except: # o except vai tratar as excessões, os casos de erro
        return 'Erro: não foi possível realizar a divisão.'

# print(div(0))