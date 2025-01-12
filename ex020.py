from random import shuffle

#Ler o nome dos quatro alunos
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

#Colocar os nomes numa lista
alunos = [aluno1, aluno2, aluno3, aluno4]

#Sortear a ordem de apresentação dos trabalhos
shuffle(alunos)

#Mostrar a ordem sorteada
print('A ordem dos sorteados é:')
for i, aluno in enumerate(alunos, start=1):
    print('{}° - {}'.format(i, aluno))
