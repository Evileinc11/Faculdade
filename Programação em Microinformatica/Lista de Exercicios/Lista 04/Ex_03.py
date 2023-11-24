'''Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), armazene-os em uma lista. Imprima os números e imprima todos os números múltiplos de 5.
'''

from random import randint

L = [0]*20
for i in range (20):
       num = randint(1, 50)
       L[i] = num
       if num % 5 == 0:
              print(num, end=', ')
print(f'\nLista -> {L}')
