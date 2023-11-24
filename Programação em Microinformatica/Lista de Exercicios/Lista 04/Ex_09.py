'''Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e peça um 
número ao usuário. Verifique se este número pertence ou não ao vetor. Imprima o vetor 
e a mensagem de número encontrado ou não'''

'''from random import randint

A = [0]*10
for i in range (10):
       num = randint(1, 50)
       A[i] = num

print(f'Vetor -> {A}')
n = int(input('Digite um número -> '))

if n in A:
       print(f'O número {n} está na lista!')
else:
       print(f'O número {n} não está na lista!')

'''

from random import randint


A = [0]*10
for i in range (10):
       num = randint(1, 50)
       A[i] = num

print(f'Vetor -> {A}')
achou = False
n = int(input('Digite um número -> '))
for i in range(10):
       if n == A[i]:
          print(f'O número {n} está na lista!')
          achou = True
          break
if achou == False:
       print(f'O número {n} não está na lista!')