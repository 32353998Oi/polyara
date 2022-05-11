from random import randint
computador = randint(1, 100)
print('tente adivinhar o numero que eu estou pensando')
print('sera que voce é capaz de acertar?')
acertou = False
tentativas = 0
while not acertou:
    pessoa = int(input('diga seu palpite:'))
    tentativas += 1
    if pessoa == computador:
        acertou = True
    else:
        if pessoa < computador:
            print('o numero escolhido é maior ')
        elif pessoa > computador:
            print('o numero escolhido é menor ')
print('acertou com {} tentativas. Parabens'.format(tentativas))




