'''
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é acutângulo, retângulo ou obtusângulo.
Observação:
Triângulo retângulo: possui um ângulo reto (90 graus).
Triângulo obtusângulo: possui um ângulo obtuso (ângulo maior que 90 graus).
Triângulo acutângulo: possui 3 ângulos agudos (ângulo menor que 90 graus).
Faça a validação para verificar se a soma dos ângulos é igual a 180;
'''
print('Informe os 3 ângulos do triângulo')
a = float(input('Ângulo 1 -> '))
b = float(input('Ângulo 2 -> '))
c = float(input('Ângulo 3 -> '))
if (a+b+c) != 180 or a == 0 or b == 0 or c == 0:
    print('Valores inválidos!!')
else:
    if a == 90 or b == 90 or c == 90:
        print('Triângulo retângulo')
    elif a > 90 or b > 90 or c > 90:
        print('Triângulo obtusângulo')
    else:
        print('Triângulo acutângulo')
