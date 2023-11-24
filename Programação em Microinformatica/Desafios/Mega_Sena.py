'''Elabore um programa em Python que gere uma SURPRESINHA, ou seja, uma aposta para a 
MEGASENA, com 6 números entre 1 e 60, sem repetição, armazenando em um vetor. Faça a 
validação. 
Após gerar a aposta, deverão ser informados pelo teclado os números do resultado da 
MEGASENA, os quais serão armazenados em um vetor de 6 posições, com números de 1 a 60, sem 
números repetidos. Faça a validação. 
Faça a ordenação dos vetores e a comparação, confira o resultado e mostre se houve ou não acertos 
para a aposta gerada. Informe ainda se houve Quadra (4 acertos), Quina (5 acertos) ou Sena (6 
acertos), mostrando os números certos'''

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