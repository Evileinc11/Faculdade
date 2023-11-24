'''
Elabore um programa em Python que declare e peça uma
matriz quadrada de 3 linhas por 3 colunas e verifique se
a matriz é simétrica em relação à diagonal principal.
A matriz simétrica é aquela em que todos os elementos
A( i , j)  =  A( j , i)  para quaisquer valores de i e j.
Assim, A[2,1] deverá ser igual a A[1,2], e A[0,2] deverá ser
igual a A[2,0] e assim por diante.
Imprimir mensagem “Matriz Simétrica” ou “Matriz não Simétrica”.
'''

M = [0] * 3
for i in range(3):
    M[i] = [0] * 3
    for j in range(3):
        M[i][j] = int(input(f"{[i]}{[j]} -> "))

print("\nMatriz informada")
for i in range(3):
    for j in range(3):
        print(f"{M[i][j]:2}",end=' ')
    print()

sim = True
for i in range(2):
    for j in range(i+1,3):
        if M[i][j] != M[j][i]:
            sim = False

if sim:
    print("\nMatriz simétrica em relação a diagonal principal")
else:
    print("\nMatriz não é simétrica em relação a diagonal principal")