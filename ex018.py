import math

#Ler o valor do ângulo em graus
a = float(input('Digite o ângulo: '))

#Converter o ângulo para radiano
rad = math.radians(a)

#Calcular o seno, cosseno e tangente
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

#Mostrar os resultados
print('O valor do seno de {} graus é: {:.2f}'.format(a,s))
print('O valor do cosseno de {} graus é: {:.2f}'.format(a, c))
print('O valor da tagente de {} graus é: {:.2f}'.format(a, t))
