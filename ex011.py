larg = float(input('Qual a largura da parede em metros: '))
altu = float(input('Qual a altura da parede em metros: '))
a = larg * altu
ltmq = a / 2
print('A dimensão da sua parede é {} x {}'.format(larg, altu))
print('A área a ser pintada é de: {} m2 e será necessário {:.1f} litros de tinta para pintar a parede toda'.format(a, ltmq))
