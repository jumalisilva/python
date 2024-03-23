# O comando print serve para mostrar uma informação ao usuário
# print('Hello world!')

# print('2 + 2')

## Variáveis
# 1) Variável string -> armazena textos e precisa de ASPAS
nome = 'Julia'

# Variável numérica 
# 2) Variável int -> armazena números inteiros
idade = 23

# 3) Variável float -> armazena números decimais
altura = 1.51

# 4) Variável booleana -> armazena True (verdadeiro) ou False (falso) e precisa começar com letra maiúscula
acordado = True

# O sinal de = significa "recebe"

# print(nome)
# print(idade)
# print(altura)
# print(acordado)

# O comando input cria uma caixa de diálogo com o usuário
# nome = input('Qual o seu nome? ')

# A vírgula serve para concatenar elementos diferentes
# print('Olá, bom dia', nome)

## Operadores aritméticos
# 1) Soma (+)
print('2 + 2 =', 2 + 2)

# 2) Subtração (-)
print('3 - 2 =', 3 - 2)

# 3) Multiplicação (*)
print('4 x 2 =', 4 * 2)

# 4) Divisão float (/)
print('7 / 2 =', 7 / 2)

# 5) Divisão inteira (//)
print('10 // 5 =', 10 // 5)

# 6) Módulo (%) -> olha somente o resto da divisão
print('3 % 2 =', 3 % 2) # isso porque, no resto dessa divisão, sobra 1

## Operadores Relacionais -> O resultado sempre vai ser True ou False
# 1) Menor que (<)
print('7 < 2 =', 7 < 2) # Sete é menor que dois?

# 2) Maior que (>)
print('7 > 2=', 7 > 2) # Sete é maior que dois?

# 3) Menor ou igual (<=)
print('7 <= 2 =', 7 <= 2) # Sete é menor ou igual a dois?

# 4) Maior ou igual (>=)
print('7 >= 2', 7 >= 2) # Sete é maior ou igual a dois?

# 5) Igualdade (==)
print('7 == 2 =', 7 == 2) # Sete é igual a dois?

# 6) Diferente (!=)
print('7 != 2 =', 7 != 2) # Sete é diferente de dois?

val = float(input('Digite um número: '))
print(val * val)