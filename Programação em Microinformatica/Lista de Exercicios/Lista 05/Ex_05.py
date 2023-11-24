'''
Faça um programa em Python que gere uma matriz 5 x 5 de
inteiros entre 1 e 50, imprima a matriz e o menor elemento
de cada coluna.
'''

from random import randint

print("Matriz gerada")
M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = randint(1,50)
        print(f"[{M[i][j]:2}]",end=" ")
    print()

print("Menor de cada coluna")
for i in range(5):
    menor = M[0][i]
    for j in range(5):
        if M[j][i] < menor:
            menor = M[j][i]
    print(f"[{menor:2}]",end=" ")