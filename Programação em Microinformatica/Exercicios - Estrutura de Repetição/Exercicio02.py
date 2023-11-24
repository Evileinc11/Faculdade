'''Escreva um programa que gere um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a saída para n = 4 seria:  
* 
**
***
****
*** 
**
*'''

n = int(input('Informe a altura -> '))

for i in range(1,n):
    for j in range(i):
        print('*', end='')
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print("=" * 50)

for i in range(1,2*n):
    if i < n:
        for j in range(i):
            print('*', end='')
    else:
        for j in range(2*n-i):
            print('*', end='')
    print()
