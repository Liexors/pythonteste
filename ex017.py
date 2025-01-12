from math import hypot
#Ler o comprimento do cateto oposto
co = float(input('Digite o comprimento do cateto oposto: '))

#Ler o comprimento do cateto adjacente
ca = float(input('Digite o comprimento do cateto adjacente: '))

#Calcular o comprimento da hipotenusa
h = hypot(co, ca)

#Mostrar o comprimento da hipotenusa
print('O comprimento da hipotenusa é: {:.2f}'.format(h))
