'''Faça um programa em Python que gere 20 elementos aleatórios (entre 1 e 50) 
armazenando no vetor A e crie outros 2 vetores B e C. O vetor B deve ter apenas os 
números pares e o vetor C deve conter apenas os números ímpares. Imprima os três 
vetores'''

from random import randint

A = [0]*20
for i in range (20):
       num = randint(1, 50)
       A[i] = num

B = []
for i in range (20):
       if A[i] % 2 == 0:
              B.append(A[i])

C = []
for i in range (20):
       if A[i] % 2 != 0:
              C.append(A[i])
print(f'Vetor A -> {A}\nVetor B -> {B}\nVetor C -> {C}')