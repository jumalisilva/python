# C) Peça ao usuário para digitar uma letra e determine se ela é uma vogal ou uma consoante.

letra = input('Digite uma letra: ')

letra = letra.lower()

if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print('A letra {} é uma vogal.' . format(letra))
else:
    print('A letra {} é uma consoante.' . format(letra))