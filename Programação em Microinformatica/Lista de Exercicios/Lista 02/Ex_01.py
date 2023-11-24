'''
Elabore um programa que leia um número (de 3 algarismos, faça a validação para aceitar apenas
números menores que 1000) e imprima se ele é ascendente. Um número é ascendente se seus algarismos
estão em ordem crescente. Por exemplo, o número 258 é ascendente, pois, 2 < 5 e 5 < 8
'''
N = int(input("Informe um número de 3 algarismos -> "))
if N < 100 or N > 999:
    print('Número inválido!!')
else:
    c = N // 100
    d = N % 100 // 10
    u = N % 10
    if c < d < u:
        print(f'{N} é um número ascendente')
    else:
        print(f'{N} não é um número ascendente')

