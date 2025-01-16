#Solicitar as notas do aluno
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
#Cálculo da média da nota
média = (nota1 + nota2) / 2
#Informa a média na tela
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
#Colocando as estruturas de condição para saber se o aluno foi reprovado, recuperação ou aprovado
if média < 5:
    print('O aluno está REPROVADO. ')
elif média >=5 and média <7:
    print('O aluno está em RECUPERAÇÃO. ')
elif média >= 7:
    print('O aluno está APROVADO.')