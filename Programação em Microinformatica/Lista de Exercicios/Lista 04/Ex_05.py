'''Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) 
armazenando em uma lista. Mostre o vetor na ordem que foi gerado e na ordem inversa'''

from random import randint

L = [0] * 10
for i in range(10):
    num = randint(1, 50)
    L[i] = num
print(f'Lista Gerada  ->',*L)
print(f'Lista Inversa ->',end=' ')
for i in range(9,-1, -1):
       print(L[i],end=' ')


''' 
L[::-1] -> inversa
fatiamento de lista
'''