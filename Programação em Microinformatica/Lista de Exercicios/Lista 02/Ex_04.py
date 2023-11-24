'''Sejam três números inteiros diferentes digitados pelo usuário, faça um programa em Python que os 
coloque em ordem crescente.'''

print('Informe três valores')
a = int(input('1º valor -> '))
b = int(input('2º valor -> '))
c = int(input('3º valor -> '))

if a > b or a > c:
    if b < c:
        a, b = b, a
    else:
        a, c = c, a
if b > c:
    b, c = c, b
print(f'Números em ordem crescente -> {a} {b} {c}')
