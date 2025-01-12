m = float(input('Uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor em metros é: {} m \nEm kilometros é: {} km  \nEm hectometros é: {} hm'.format(m, km, hm))
print('Em decametros é: {} dam \nEm decimetros é: {:.0f} dm \nEm centímetros é: {:.0f} cm \nEm milímetros é: {:.0f} mm'.format(dam, dm, cm, mm))
