'''
Elabore um programa para mostrar a sequência dos N primeiro
números da série de Fibonacci:
1   1   2   3   5   8   13   21   34   55   89 ....
Sempre o próximo elemento é a soma dos dois anteriores, assim,
no exemplo o próximo é 144.
'''

N = int(input("Informe quantos termos serão exibidos da série de Fibonacci -> "))
A = 0
B = 1
C = 1
cont = 1
while cont <= N:
    print(C,end='  ')
    C = A + B
    A = B
    B = C
    cont += 1