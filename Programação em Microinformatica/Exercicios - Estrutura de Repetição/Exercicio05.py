'''Faça um programa em Python, que calcule o quadrado de um número usando o método que define que o quadrado de um número positivo n é igual à soma dos n primeiros números ímpares. 

Exemplo:
32 = 1 + 3 + 5 = 9    
62 = 1 + 3 + 5 + 7 + 9 + 11 = 36
92 = 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 = 81 
'''

n = int(input('Digite um número -> '))
impar = 1
soma = 0
for i in range (n):
        soma += impar
        impar += 2
print(f'{n}² = {soma}')