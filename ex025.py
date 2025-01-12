#Solicita ao usuário que digite o seu nome
nome_completo = str(input('Digite o nome completo: ').strip())

#Verifica se o nome contém 'Silva'
tem_silva = 'silva' in nome_completo.lower()

#Exibir o resultado
if tem_silva:
    print('Você tem Silva no nome.')
else:
    print('Você não tem Silva no nome.')
