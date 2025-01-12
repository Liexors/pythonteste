n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('O menor número é {:.0f} '.format(menor))
print('O maior número é {:.0f} '.format(maior))
