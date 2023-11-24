n = int(input('Digite um número -> '))
impar = 1
soma = 0
for i in range (n):
        soma += impar
        impar += 2
print(f'{n}² = {soma}')