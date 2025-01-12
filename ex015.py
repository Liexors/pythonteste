km = float(input('Quantos kilometros foram percorridos com o veículo? '))
d = int(input('Quantos dias o carro ficou alugado? '))
p = (60 * d) + (0.15 * km)
print('O total a pagar é R$ {:.2f}'.format(p))
