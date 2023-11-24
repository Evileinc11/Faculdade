'''Elabore um programa em Python que gere uma matriz 5x5 e calcule e mostre a diagonal principal 
e a secundária'''

from random import randint

print('Matriz Gerada')
m = []
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(randint(1,50))
        print(f'[{m[i][j]:02}]',end=' ')
    print()

print('\nDiagonal Principal')
for i in range(5):
    print(f'[{m[i][i]:02}]', end=' ')

print()
for i in range(5):
    for j in range(5):
        if i == j:
            print(f'[{m[i][j]:02}]',end=' ')
        else:
            print('[  ]', end=' ')
    print()

print('\nDiagonal Secundária')
for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(f'[{m[i][j]:02}]',end=' ')
        else:
            print('[  ]', end=' ')
    print()

print('\nTriângulo inferior em relação a DP')
for i in range(5):
    for j in range(5):
        if i > j:
            print(f'[{m[i][j]:02}]',end=' ')
        else:
            print('[  ]', end=' ')
    print()