'''
Faça um programa em Python que gere uma matriz 3 x 3 de
inteiros aleatórios entre 1 e 50, imprima a matriz e a média
de todos os elementos.
'''

from random import randint
mat = []
soma = 0
print("Matriz gerada")
for i in range(3):
    mat.append([])
    for j in range(3):
        mat[i].append(randint(1,50))
        soma += mat[i][j]
        print(f"{mat[i][j]:2}",end=" ")
    print()

media = soma / 9
print(f"\nMédia dos números = {media:.2f}")
