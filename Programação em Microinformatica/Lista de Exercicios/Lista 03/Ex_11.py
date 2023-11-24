'''
O número 3025 tem a seguinte característica:
	30 + 25 = 55
	55^2 = 3025

Elabore um programa para mostrar todos os números de 4
algarismos que possuem esta mesma característica.
'''

for num in range(1000, 10000):
    if (num // 100 + num % 100)**2 == num:
        print(num)