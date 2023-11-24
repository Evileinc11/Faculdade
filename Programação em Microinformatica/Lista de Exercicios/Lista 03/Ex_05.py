'''Escreva um programa para ler 10 números do usuário e calcular a soma dos números pares e a 
soma dos números ímpares'''

c = 1
sp = si = 0
while c <= 10 :
    num = int(input('Número -> '))
    if num % 2 == 0:
        sp += num
    else:
        si += num
    c += 1
print('Soma dos números pares   ->',sp)
print('Soma dos números ímpares ->',si)