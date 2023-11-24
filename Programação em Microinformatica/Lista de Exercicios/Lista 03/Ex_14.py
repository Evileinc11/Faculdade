'''
Uma forma de verificar se um número é um quadrado perfeito é
calculando a soma dos números ímpares, veja:

1  quadrado perfeito
1 + 3 = 4  quadrado perfeito
1 + 3 + 5 = 9  quadrado perfeito
1 + 3 + 5 + 7 = 16  quadrado perfeito
1 + 3 + 5 + 7 + 9 = 25  quadrado perfeito
1 + 3 + 5 + 7 + 9 + 11 = 36  quadrado perfeito
E assim por diante...

Elabore um programa que leia um número inteiro e verifique se ele é
ou não quadrado perfeito.
'''
N = int(input("Informe um número -> "))
soma = 0
impar = 1
while soma < N:
    soma += impar
    impar += 2
if soma == N:
    print(f"{N} é um quadrado perfeito")
else:
    print(f"{N} não é um quadrado perfeito")