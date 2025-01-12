#Solicite que o usuário digite uma frase
frase = str(input('Digite uma frase: ')).strip()

#Exibe as respostas
print('Analisando a frase: {}'.format(frase))
print('A letra "a" aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira letra "a" aparece na posição {}.'.format(frase.lower().find('a')))
print('A última letra "a" aparece na posição {}.'.format(frase.lower().rfind('a')))
