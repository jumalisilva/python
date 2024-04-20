# Agora adicione ao programa anterior (atividade05B) uma tentativa máxima de 4 vezes para errar a senha

senhaUsuario = int(input('Digite uma senha numérica: '))
senhaCorreta = 12345
i = 4

while (i >= 0):
    if (senhaUsuario != senhaCorreta):
        print('Senha incorreta, {} tentativa(s) restantes. Tente novamente.' . format(i))
        senhaUsuario = int(input('Digite uma senha numérica: '))
        i -= 1
    elif (senhaUsuario == senhaCorreta):
        print('Você acessou o sistema!')
        break