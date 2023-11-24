'''Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) sem 
números repetidos. Imprima o vetor'''

from random import randint

L = []
while len(L) < 10:
       x = randint(1, 50)
       if x not in L:
               L.append(x)
L.sort()
print(L)