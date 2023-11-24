'''
Construa um programa que verifique
se um número fornecido pelo usuário é primo ou não.
'''

n = int(input("Informe um número para verificar se é primo -> "))
primo = True
if -1 <= n <= 1:
    primo = False
for div in range(2, n//2+1):
    if n % div == 0:
        primo = False
        break
if primo:
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")
