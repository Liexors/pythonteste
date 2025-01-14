from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = input('Qual o seu sexo [M/ F]: ').upper()
idade = atual - nasc
if sexo == 'M':
    print('Você informou que é do sexo masculino, sendo assim.....')
    print('Quem nasceu no ano {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que ALISTAR URGENTEMENTE !!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda falta {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
elif sexo == 'F':
    print('Você informou que é do sexo feminino, sendo assim não é obrigatório o seu alistamento')
else:
    print('Opção inválida. Por favor, informe "M ou F". ')
