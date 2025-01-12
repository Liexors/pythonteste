#Solicite ao usuário que digite 3 números
a = int(input('Digite o primeiro número : '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

#Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

#Informando o resultado
print('O menor valor digitado é {} '.format(menor))
print('O mair valor digitado é {} '.format(maior))
