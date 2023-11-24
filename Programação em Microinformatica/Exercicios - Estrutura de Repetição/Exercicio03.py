'''Faça um programa em Python que gere um triângulo de altura e lados n e base 2*n-1. Por exemplo, a saída para n = 6 seria: 
*
***
*****
*******
*********
***********
'''

n = int(input('Informe a altura -> '))

for i in range(1,2*n,2):
    linha = ''
    for j in range(i):
        linha += '*'
    print(linha.center(2*n))
