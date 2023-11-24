'''Elabore um programa em Python que gere uma matriz aleatória (9x9), com números entre 0 e 
10, imprima-a. Após, peça o quadrante desejado e imprima os elementos desse quadrante.
'''

from random import randint
mat=[]

print("\nNúmeros gerados")
for i in range(9):
    mat.append([])
    for j in range(9):
        mat[i].append(randint(0,10))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()

quad = int(input("Informe o quadrante -> "))
if quad == 1:
    for i in range(0,3):
        for j in range(0,3):
            print("[{:2}] ".format(mat[i][j]), end='')
        print()
elif quad == 2:
    for i in range(0,3):
        for j in range(5,9):
            print("[{:2}] ".format(mat[i][j]), end='')
        print()
elif quad == 3:
    for i in range(5,9):
        for j in range(0,3):
            print("[{:2}] ".format(mat[i][j]), end='')
        print()
elif quad == 4:
    for i in range(5,9):
        for j in range(5,9):
            print("[{:2}] ".format(mat[i][j]), end='')
        print()
else:
    print("Quadrante inválido!!")