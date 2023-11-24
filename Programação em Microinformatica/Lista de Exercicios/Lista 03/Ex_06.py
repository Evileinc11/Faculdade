'''Igual ao exercício anterior, mas pedir antes do laço a quantidade de números a serem lidos'''

c = 1
sp = 0
si = 0
q = int(input('Digite a quantidade de números a serem lidos -> '))
while c <= q:
    num = int(input('Digite o numero -> '))
    if num % 2 == 0:
        sp += num
    else:
        si += num
    c +=1
print(f'A soma dos numeros pares é -> {sp}')
print(f'A soma dos números ímpares é -> {si}')