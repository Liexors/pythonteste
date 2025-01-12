nome = str(input('Qual o seu nome? ')) #Solicite ao usuário que digite seu nome

if nome == 'Rafael':  #Algoritimo para condição aninhada.
    print('Uau! que nome lindo ^ ^ ! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
else:
    print('Seu nome é tão normal kkkk !')

#Resultado que sempre aparecerá, independente da condição ser alcançada ou não
print('Tenha um bom dia, {} !'.format(nome))
