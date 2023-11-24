'''Escreva um programa que armazene um valor de entrada em uma variável A e outro em uma variável 
B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que 
o valor que está em A passe para B e vice-versa. Ao final escrever os valores que ficaram armazenados 
nas variáveis'''

a = int(input("Informe um valor    -> "))
b = int(input("Informe outro valor -> "))
print(f'Valores informados -> 1º: {a} e 2º: {b}')
#a, b = b, a
c = a
a = b
b = c
print(f'Valores trocados   -> 1º: {a} e 2º: {b}')
