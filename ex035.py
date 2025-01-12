#Verificar se as retas podem formar um triângulo
def eh_triangulo(r1, r2, r3):
    if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
        return True
    else:
        False

#Solicitar ao usuário para digitar o comprimento das 3 retas
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento d terceira reta: '))

#Chamar a função de verificação do triângulo
if eh_triangulo(r1, r2, r3):
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
