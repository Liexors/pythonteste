peso = float(input('Qual o seu peso em Kg? ' ))
altura = float(input('Qual a sua altura em Metros? ' ))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso normal ')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL ')
elif 25 <= imc < 30:
    print('Você está SOBREPESO ')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!! ')
elif 40 <= imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado! ')
