'''
Faça um programa em Python que leia uma matriz 2 x 3 de inteiros,
imprima a matriz e a soma de todos os elementos.
'''

mat = []
soma = 0
for i in range(2):
    mat.append([])
    print(f"{i+1}ª Linha")
    for j in range(3):
        mat[i].append(int(input(f"[{i}][{j}] -> ")))
        soma += mat[i][j]

print("\nNúmeros informados")
for i in range(2):
    for j in range(3):
        print(f"{mat[i][j]:2}",end=' ')
    print()

print(f"\nSoma de todos os números -> {soma}")