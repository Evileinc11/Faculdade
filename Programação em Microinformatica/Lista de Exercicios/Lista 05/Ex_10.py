'''Escreva um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 
a 50, peça um número de uma linha qualquer, entre 0 e 9, e copie os elementos dessa linha para 
um vetor. Imprima a matriz e o vetor'''

from random import randint
mat=[]

print("\nNúmeros gerados")
for i in range(10):
    mat.append([])
    for j in range(10):
        mat[i].append(randint(1,50))
        print("[{:2}] ".format(mat[i][j]),end='')
    print()

while True:
    lin = int(input("Informe o número da linha (0 a 9) -> "))
    if lin not in range(10):
        print("Linha inválida, digite novamente")
    else:
        break

vet = mat[lin]
print(vet)
