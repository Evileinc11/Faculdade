'''Faça um programa em Python que gere 10 números aleatórios (entre 1 e 50), armazeneos em uma lista. Imprima os números e calcule quantos são números pares e quantos 
são números ímpares.'''

from random import randint

L = [0]*10
imp = 0
par = 0
for i in range (10):
       num = randint(1, 50)
       L[i] = num
       if num % 2 == 0:
              par +=1
       if num % 2 != 0:
              imp += 1
print(f'Lista -> {L}\nTotal de números ímpares = {imp}\nTotal de números pares = {par}')