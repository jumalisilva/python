# Função - se declara com def, seguido do nome da função e parênteses. toda função pode ter ou não parâmetros dentro do ().
# Parâmetros são uma espécie de "variável" conhecida apenas dentro daquela função
# A palavra return indica o que a função precisa devolver ao final da execução

# def quadrado (x):
#     return x * x

# print(quadrado(8))
# print(quadrado(2))

def soma (a, b):
    soma = a + b
    return  soma

def sub (c, d):
    sub = c - d
    return sub

def result (x, y):
    return soma(x, x) - sub(y, x)

print(result(1, 2))