'''
Elabore um programa que calcule N! (fatorial de N),
sendo que o valor inteiro de N é fornecido pelo usuário.
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

fat = 1
N = int(input("Informe o valor para cálculo do fatorial -> "))
for num in range(2,N+1):
    fat *= num
print(f"O fatorial de {N} é {fat}")

fat = 1
print(f"{N}! =",end=" ")
for num in range(N, 0, -1):
    fat *= num
    print(f"{num} x",end=" ")
print(f"\b\b= {fat}")