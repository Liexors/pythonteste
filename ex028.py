from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"

#Texto para melhorar a interação com o usuário, deixar mais divertido
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar....')
print('-=-' * 20)

#Solicite ao jogador que digite um número entre 0 e 5
jogador = int(input('Em que número eu pensei? '))
print('Será que você acertou?.....deixa eu lembrar...')
sleep(3)

if jogador == computador:
    print('O que !!!!! Como você advinhou? Tá lendo mentes agora? ')
else:
    print('Eu ganhei hauhauha! Eu pensei no número {} e não no {}! '.format(computador, jogador))
