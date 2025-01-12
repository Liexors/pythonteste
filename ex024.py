#Digitar o nome da cidade
nome = str(input('Digite o nome da sua cidade: ').strip())

#Verificar se o nome da cidade começa com 'Santo'
comecacomsanto = nome[:5].lower() == 'santo'

#Exibir o resultado
if comecacomsanto:
    print('A cidade começa com santo. ')
else:
    print('A cidade não começa com santo. ')

