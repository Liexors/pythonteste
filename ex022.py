#Digite o nome completo
nome = str(input('Digite o nome completo: ')).strip()

#Resultado todo em maiúscula
print('Seu nome em maiúscula é: {}.'.format(nome.upper()))

#Resultado todo em minúscula
print('Seu nome em minúscula é: {}.'.format(nome.lower()))

#Quantas letras tem no total sem contar os espaços
print('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))

#Quantas letras tem o primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
