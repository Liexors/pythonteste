from datetime import date #Importar biblioteca de manipulação de datas
#Criando a variável pro tempo atual
atual = date.today().year
#Solicitando que o usuário digite o ano de nascimento
nascimento = int(input('Ano do nascimento: '))
#Variável pra calcular a idade
idade = atual - nascimento
#resultado mostrado na tela
print('O atleta tem {} anos.'.format(idade))
#Adicionado a estrutura de condição para classificar os nadadores de acordo com a idade
if idade <= 9:
    print('Classificação: MIRIM.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JÚNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')
