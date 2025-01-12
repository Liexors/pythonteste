from random import shuffle
#Ler o nome dos quatros alunos
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

#Lista dos alunos
lista = [aluno1, aluno2, aluno3, aluno4]

#Utilizar o shuffle para sortear os alunos
shuffle(lista)

#Ler o resultado do sorteio
print('A ordem dos alunos que irão apresentar os trabalhos são: ')
print(lista)