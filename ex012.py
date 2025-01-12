pp = float(input('Digite o valor do produto: R$ '))
pordesc = 5
calcdesc = pp * pordesc / 100
valorf = pp - calcdesc
print('O preço atual do produto é: {} , com 5% de desconto o produto sai a: R$ {:.2f}'.format(pp, valorf))
