'''Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e ordene 
os números em ordem ascendente. Imprima o vetor antes e após a ordenação. Pesquise 
sobre os métodos de ordenação.'''

from random import randint
from time import time

tam = 200
L = []
for i in range (tam):
       L.append(randint(1, 50))
M = L.copy()

ini = time()
L.sort()
fim = time()
print('Tempo usado -> ', fim-ini)

#Bubble sort
ini = time()
for i in range (tam):
       for j in range (i+1, tam):
              if M[i] > M[j]:
                     M[i], M[j] = M[j], M[i]
fim = time()
print(fim-ini)