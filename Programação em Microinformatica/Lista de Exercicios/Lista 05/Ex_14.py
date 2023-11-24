'''Faça um programa em Python que gere as 5 notas (de 0 a 10) de 10 atletas em uma competição. 
Armazene em uma matriz 10x5. Após, calcule a média de cada atleta descartando a maior e 
menor nota obtida e diga qual atleta venceu a competição, ou seja, o número da linha.'''

from random import randint
mat = []

for i in range(10):
    mat.append([])
    for j in range(5):
        mat[i].append(randint(0,10))
    mat[i].sort()
    media = 0
    for j in range(1, 4):
        media += mat[i][j]
    media /= 3
    mat[i].append(media)

linha = 0

for i in range(1,10):
    if mat[i][5]> mat[linha][5]:
        linha = i

for i in range(10):
    for j in range(5):
        print("{:2}".format(mat[i][j]),end=" ")
    if i == linha:
        print(" -> Média = {:.2f} -> Campeão!!".format(mat[i][5]))
    else:
        print(" -> Média = {:.2f}".format(mat[i][5]))
