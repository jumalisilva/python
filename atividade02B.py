# B) Crie um programa que peça ao usuário para digitar dois números e, em seguida, informe qual deles é o maior.
    
num1 = float(input('Digite o primeiro número (num1): '))
num2 = float(input('Digite o segundo número (num2): '))

if (num1 > num2):
    print('{} é maior que {}.' . format(num1, num2))
elif (num1 < num2):
    print('{} é maior que {}.' . format(num2, num1))
else:
    print('{} e {} são iguais.' . format(num1, num2))