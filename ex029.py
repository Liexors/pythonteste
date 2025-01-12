velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade > 80:
    print('Multado!! Você excedeu o limite de velocidade permitido de 80 KM/H ')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f} '.format(multa))
print('Tenha uma boa viagem e dirija com segurança!!')
