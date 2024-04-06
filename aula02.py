## Operadores Lógicos

# AND -> no operador AND, precisamos que todas as condições analisadas sejam True para se ter um resultado True, caso contrário, o resultado será False

# print("True and True =", True and True)
# print("True and False =", True and False)
# print("False and True =", False and True)
# print("False and False =", False and False)

# Verificar se uma pessoa pode dirigir
temCarro = True
temHabilitacao = True

# print(temCarro == True and temHabilitacao == True)

# OR -> no operador OR, se for encontrado pelo menos uma das condições como True, o resultado será True, só teremos um False se toda as condições forem False

# print("True or True =", True or True)
# print("True or False =", True or False)
# print("False or True =", False or True)
# print("False or False =", False or False)

# Verificar se o usuário comprou um filme
compraFilme = True
assinante = False

# print(compraFilme == True or assinante == True)

## Condicionais (IF/ELSE/ELIF)

# Verificando se uma pessoa é maior de idade
idade = 20

if (idade >= 18): # verifico se a idade é maior ou igual a 18,
    print("É maior de idade") # mostro o texto "é maior de idade"
else: # se a idade não for maior ou igual a 18,
    print("Não é maior de idade") # mostro o texto "não é maior de idade"