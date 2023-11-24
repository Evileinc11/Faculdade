'''Faça um programa em Python que, para o intervalo de 100 a 999, calcule e imprima a soma de seus algarismos caso seja par e o produto de seus algarismos, caso seja ímpar. Por exemplo, para o número 136, deverá calcular e imprimir 1+3+6 que é 10 e, para o número 353, deverá calcular e imprimir 3*5*3 que é 45. 

num = 136
c = num // 100
d = num %100 // 10
u = num % 10
'''

for i in range (100, 1000):
    num = i
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    if i % 2 == 0:
        soma = c + d + u
        print(f'A variavel {i} -> {soma}')
    else:
        mult = c * d * u
        print(f'A variavel {i} -> {mult}')

