#Deixa o programa mais bonito
print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

#Solicite ao usuário que digite os valores de cada reta
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo! ')
else:
    print('Os segmentos NÃO PODEM formar um triângulo! ')
