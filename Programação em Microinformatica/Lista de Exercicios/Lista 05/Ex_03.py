'''Faça um programa em Python que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e 50, 
imprima a matriz e a soma de todos os elementos de cada linha.
'''

from random import randint

m = []
for i in range(5):
    soma = 0
    m.append([])
    for j in range(5):
        m[i].append(randint(1,50))
        soma += m[i][j]
        print(f'{m[i][j]:02}',end=' ')
    print('-> ',soma)

