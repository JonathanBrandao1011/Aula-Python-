notaum = int(input('Primeira nota:'))
notadois = int(input('Segunda nota:'))
media = (notaum + notadois)/2
if media >= 6:
    print('Aprovado')
elif media < 4:
    print('Reprovado')
else:
    print('Recuperação')
