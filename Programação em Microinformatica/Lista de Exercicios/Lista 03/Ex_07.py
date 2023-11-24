'''Escreva um programa que gere um conjunto de 20 números inteiros aleatórios entre 1 e 50 e 
mostre qual foi o maior e o menor valor gerado.'''

from random import randint
c = 1
maior = 0
menor = 51
while c <= 20:
    n = randint(1, 50)
    print(n,end=' ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1

print(f'\nMaior número = {maior}')
print(f'Menor número = {menor}')