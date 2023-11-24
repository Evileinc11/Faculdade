'''
Elabore um programa em Python que leia duas matrizes
A (mxn) e B (pxq) e calcule e mostre a matriz Python
que é a soma de A com B (caso a soma seja possível).
'''
from random import randint

print("Entre com as dimensões da Matriz A")
m = int(input("Qtd de linhas -> "))
n = int(input("Qtd de colunas -> "))

print("Entre com as dimensões da Matriz B")
p = int(input("Qtd de linhas -> "))
q = int(input("Qtd de colunas -> "))

if m == p and n == q:
    print("Matriz A gerada")
    A = [0] * m
    for i in range(m):
        A[i] = [0] * n
        for j in range(n):
            A[i][j] = randint(1,20)
            print(f"{A[i][j]:2}",end=" ")
        print()

    print("\nMatriz B gerada")
    B = [0] * p
    for i in range(p):
        B[i] = [0] * q
        for j in range(q):
            B[i][j] = randint(1,20)
            print(f"{B[i][j]:2}",end=" ")
        print()

    print("\nMatriz C calculada (soma)")
    C = [0] * m
    for i in range(m):
        C[i] = [0] * n
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
            print(f"{C[i][j]:2}",end=" ")
        print()
else:
    print("Não é possível somar matriz com dimensões diferentes")