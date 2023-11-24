'''
Elabore um programa em Python que gere uma matriz 4x6 e
calcule e mostre a sua matriz transposta equivalente.
'''

from random import randint

print("Matriz gerada")
M = [0] * 4
for i in range(4):
    M[i] = [0] * 6
    for j in range(6):
        M[i][j] = randint(1,50)
        print(f"{M[i][j]:2}",end=" ")
    print()

#Apenas imprimindo invertendo linha com coluna
print("\nMatriz transposta")
for i in range(6):
    for j in range(4):
        print(f"{M[j][i]:2}",end=" ")
    print()

#criando outra variável do tipo matriz para receber a matriz transposta
print("\nMatriz transposta")
T = [0] * 6
for i in range(6):
    T[i] = [0] * 4
    for j in range(4):
        T[i][j] = M[j][i]
        print(f"{T[i][j]:2}", end=" ")
    print()