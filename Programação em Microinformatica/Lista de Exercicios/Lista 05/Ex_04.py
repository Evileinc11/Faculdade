'''
Faça um programa em Python que gere uma matriz 5 x 5 de
inteiros entre 1 e 50, imprima a matriz e o menor elemento
de cada linha.
'''

from random import randint
mat = []

for i in range(5):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(1,50))

print("Matriz gerada")
for i in range(5):
    menor = mat[i][0]
    for j in range(5):
        if mat[i][j] < menor:
            menor = mat[i][j]
        print(f"{mat[i][j]:2}",end=" ")
    print(f" -> O menor número da linha {i} é {menor}")