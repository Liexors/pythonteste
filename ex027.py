n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer !')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
