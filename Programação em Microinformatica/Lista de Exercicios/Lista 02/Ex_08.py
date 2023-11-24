'''
Leia o salário de um trabalhador e o valor da prestação de um
empréstimo. Se a prestação for maior que 20% do salário imprima:
Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
'''

salario = float(input("Informe o salário -> "))
valor = float(input("Informe o valor da prestação -> "))
parc = salario*0.2
if valor>parc:
    print("Empréstimo não concedido!!")
else:
    print("Empréstimo concedido!!")
