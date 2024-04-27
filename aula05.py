# Listas
frutas = ["maçã", "uva", "banana"]
# print(frutas)
# print(frutas[2]) # vai imprimir banana pois banana está na posição 2

# for fruta in frutas:
    # print(fruta)

# pessoa = ["Julia", 21, 1.65, True, [5, "Sim"]]

# for i in pessoa:
   # print(i)

# print(pessoa[4][1]) # para acessar o segundo elemento da sub lista, que está na posição 1

numeros = [10, 20, 30]

# for i in numeros:
#     print(i + 5)

numeros.append(40) # append adiciona elementos na última posição da minha lista
print(numeros)

# insert(index, valor) - adiciona o elemento na posição desejada
numeros.insert(2, 25)
print(numeros)