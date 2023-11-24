'''Faça um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 a 
50 e copie para um vetor de 10 elementos, os números da diagonal principal. Imprima a matriz 
e o vetor.
'''

from random import randint
mat=[]
print("\nNúmeros gerados")
for i in range(10):
    mat.append([])
    for j in range(10):
        mat[i].append(randint(1,50))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()

vet = []
for i in range(10):
    vet.append(mat[i][i])
print(vet)
