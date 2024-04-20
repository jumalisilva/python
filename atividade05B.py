# Faça um programa que solicite ao usuário que insira uma senha. O programa deve permitir que o usuário tente entrar com a senha até que ele acerte a senha correta.

senhaUsuario = int(input('Digite uma senha numérica: '))
senhaCorreta = 12345

if (senhaUsuario == senhaCorreta):
    print('Você acessou o sistema!')
else:
    print('Senha incorreta. Tente novamente.')