'''
Faça um programa que receba um
número inteiro e verifique se este número é par ou ímpar.
'''

num = int(input("Informe um número -> "))
if num % 2 == 0:
    print(f"O número {num} é PAR")
else:
    print(f"O número {num} é ÍMPAR")
