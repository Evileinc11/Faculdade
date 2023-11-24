'''
Escreva um programa em Python que leia o valor de 3 lados de um triângulo e escreva se o triângulo é
equilátero, isósceles ou escaleno.
Observação:
Triângulo equilátero: possui três lados iguais.
Triângulo isósceles: possui dois lados iguais.
Triângulo escaleno: possui três lados diferentes.
Faça a validação para verificar se os valores dos lados formam um triângulo. Todo lado tem que ser menor
que a soma dos outros dois.
'''
print('Informe o valor dos 3 lados de um triângulo')
a = float(input('Lado 1 -> '))
b = float(input('Lado 2 -> '))
c = float(input('Lado 3 -> '))
if a < b + c and b < a + c and c < a + b:
    if a == b and b == c: # a == b == c
        print('Triângulo equilátero')
    elif a != b and b != c and a != c: # a != b != c != a
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
else:
    print('As medidas informadas não formam um triângulo')
