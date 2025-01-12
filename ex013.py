sal = float(input('Digite o salário: R$  '))
novo = sal + (sal * 15 / 100)
print('Seu salário atual é de: R$ {} , com o aumento de 15% fica em R$ {:.2f} '.format(sal, novo))
