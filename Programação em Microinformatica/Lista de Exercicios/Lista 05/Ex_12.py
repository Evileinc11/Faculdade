'''
Faça um programa em Python que gere uma matriz 5x5 com valores entre 1 e 50.
Imprima a matriz e troque uma linha por outra linha informada pelo usuário.
Mostre a matriz após a troca.
'''
from random import randint
print("Matriz gerada")
m = []
for i in range(5):
    m.append([])
    for j in range(5):
        m[i].append(randint(1,50))
        print(f"{m[i][j]:2}", end = " ")
    print()

print("Informe 2 linhas para efetuar a troca entre elas")
while True:
    lin1 = int(input("Linha 1 >> "))
    if lin1 in range(5):
        break
    print("Valor inválido!! Digite entre 0 e 4...")
while True:
    lin2 = int(input("Linha 2 >> "))
    if lin2 in range(5):
        break
    print("Valor inválido!! Digite entre 0 e 4...")

m[lin1], m[lin2] = m[lin2], m[lin1]

print(f"Matriz com as linhas {lin1} e {lin2} trocadas")
for i in range(5):
    for j in range(5):
        print(f"{m[i][j]:2}", end = " ")
    print()
