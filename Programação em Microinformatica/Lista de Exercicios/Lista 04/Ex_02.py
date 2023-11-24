'''Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50), armazeneos em uma lista. Imprima os números e calcule a média apenas dos números pares'''

from random import randint

L = [0]*20
par = 0
med = 0
contP = 0
for i in range (20):
       num = randint(1, 50)
       L[i] = num
       if num % 2 == 0:
              contP += 1
              par += num
              med = par / contP
print(f'Lista -> {L}\nA média dos números pares é = {med}')