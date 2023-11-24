'''Faça um programa que o usuário informe os valores dos catetos de um triângulo retângulo e ao final 
escreva a sua hipotenusa'''

from math import sqrt

print('Programa para calcular a hipotenusa de um triângulo retângulo')
b = float(input('Cateto adjacente -> '))
c = float(input('Cateto oposto -> '))
a = sqrt(b*b + c*c)
print(f'A hipotenusa é {a:.1f}')