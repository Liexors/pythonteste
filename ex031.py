distância = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.0f} KM '.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem é de R$ {:.2f}'.format(preço))
