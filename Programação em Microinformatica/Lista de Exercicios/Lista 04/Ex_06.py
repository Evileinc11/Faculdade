'''Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) 
armazenando na lista A e um valor x. Criar o vetor B contendo os elementos do vetor A 
multiplicados por x. Imprima os dois vetores.'''

from random import randint

val = randint(1, 50)
A = [0]*10
for i in range (10):
       num = randint(1, 50)
       A[i] = num
B = [0]*10
for i in range (10):
       B[i] = val * A[i]
print(f'Valor X -> {val}\nLista A -> {A}\nLista B -> {B}')