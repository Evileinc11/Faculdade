'''
Escreva um programa que peça a Nota 1 (N1) e a Nota 2 (N2) de
10 alunos e a cada aluno mostre a média M, onde M=(N1+N2)/2.
'''

for i in range(1,11):
    print(f"Informe as duas notas do aluno {i}")
    while True:
        n1 = float(input('Nota 1 -> '))
        if n1 not in range(0, 11):
            print("Nota 1 inválida, digite novamente dentro do intervalo de 0 a 10...")
        else:
            break
    while True:
        n2 = float(input('Nota 2 -> '))
        if n2 not in range(0, 11):
            print("Nota 2 inválida, digite novamente dentro do intervalo de 0 a 10...")
        else:
            break
    m = (n1 +n2) / 2
    print(f"Média = {m:.2f}")
    print('~' * 40)