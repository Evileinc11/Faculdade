from random import randint

L = []
while len(L) < 6:
       x = randint(1, 60)
       if x not in L:
               L.append(x)
L.sort()
'''print(f'Surpresinha -> {L}')'''
print('Informe os resultados da Mega Sena: ')
M = []
c = 1
while len(M) < 6:
       x = int(input(f'{c}° Número -> '))
       if x < 1 or x > 60:
           print('Número inválido!')
       else:
         if x not in M:
               M.append(x)
               c += 1
         else:
           print('Número já inserido!')
M.sort()
print(f'Números da Mega Sena -> {M}')
cont = 0
for i in range (6):
    if L[i] in M:
        cont += 1
if cont == 4:
    print(f'Você acertou uma quadra!')
elif cont == 5:
    print(f'UAU! Você acertou a QUINA!')
elif cont == 6:
    print(f'PARABÉNS! Você acertou a SENA!')
if cont == 0:
    print('Você não acertou nenhum número :( Mais sorte na próxima vez!')
else:
    print(f'Você acertou {cont} números!')