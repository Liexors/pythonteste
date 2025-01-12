casa = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f}, em {} anos, '.format(casa, anos), end='')
print(' a prestação será de {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO ')
else:
    print('Empréstimo NEGADO!!')
