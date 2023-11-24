'''Escreva um programa em Python que gere uma matriz M[5][5], com números aleatórios entre 
1 e 50. Imprima a matriz. A seguir, troque os elementos da diagonal principal com os elementos 
da diagonal secundária. Imprima a nova matriz'''

from random import randint
mat=[]

print("\nNúmeros gerados")
for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,50))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()

for i in range(5):
    mat[i][i],mat[i][4-i] = mat[i][4-i],mat[i][i]

print("\nDiagonais trocadas")
for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,50))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()