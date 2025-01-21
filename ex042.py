#Solicitar que o usuário digite os 3 segmentos
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
#Para saber se 3 retas podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end= '')

    #Aqui usei um if dentro de outro if para verificar se pode ser equilátero, escaleno e isódceles
    if r1 == r2 == r3:
        print('EQUILÁTERO!') #Mostra na tela Equilátero
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!') #Mostra na tela Escaleno
    else:
        print('ISÓSCELES!') #Mostra na tela Isósceles

#Informação na tela de quando as retas não formarem um trinângulo
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo! ')
