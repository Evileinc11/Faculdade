'''
Escreva um programa que, dados dois números inteiros,
mostre na tela o maior deles,
assim como a diferença existente entre ambos.
'''

print("Informe 2 valores")
a = int(input('1º -> '))
b = int(input('2º -> '))
if a > b:
    print(f"{a} é maior que {b} e a diferença entre eles é {a-b}")
elif b > a:
    print(f"{b} é maior que {a} e a diferença entre eles é {b-a}")
else:
    print("São iguais. Não há diferença entre eles.")
