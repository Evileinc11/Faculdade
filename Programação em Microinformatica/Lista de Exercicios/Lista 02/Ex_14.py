'''Jogo da Roleta (Simulador)
Pesquisa: Método para gerar um número aleatório
Dados de entrada:
Valor da aposta em R$.
Número a ser apostado (1 a 36).
O programa deverá sortear um número aleatório e as seguintes regras deverão ser consideradas:
▪ Se o apostador acertar o número, imprimir o valor ganho sendo 5 vezes o valor apostado;
▪ Case ele erre, mas acertar a dúzia, isto é, Número da Aposta estiver entre (1 e 12) e o Número 
Sorteado também estiver entre (1 e 12) ou Número da Aposta estiver entre (13 e 24) e o Número 
Sorteado também estiver entre (13 e 24) ou Número da Aposta estiver entre (25 e 36) e o Número 
Sorteado também estiver entre (25 e 36), imprimir o valor ganho sendo 3 vezes o valor da aposta;
▪ Caso ainda erre, mas acertar a paridade, isto é, o Número da Aposta é par e o Número Sorteado 
também for par ou Número da Aposta é ímpar e o Número Sorteado também for ímpar, imprimir o 
valor ganho sendo o dobro do valor da aposta.
▪ Caso erre ainda, ele perde a quantia apostada.'''

from random import randint

print('!Jogo da Roleta!')
print('~' * 40)
valor = float(input('Irforme o valor que deseja apostar -> '))
na = int(input('Em qual número quer apostar? [1-36] -> '))
if na < 1 or na > 36:
    print('Número inválido!')
else:
    ns = randint(1,36)
    print(ns)
    if na == ns:
        print(f'Acertou!!! ganhou 5 vezes o valor apostado = R${ (valor * 5):.2f}')
    elif (1<=na<=12 and 1<=ns<=12) or (13<=na<=24 and 13<=ns<=24) or (25<=na<=36 and 25<=ns<=36):
        print(f'Acertou a dúzia!! Ganhou 3 vezes o valor da aposta + R${(valor * 3):.2f}')
    elif na % 2:
        print(f'Acertou a paridade!! Ganhou 2 vezes o valor da aposta = R${(valor * 2):.2f}')
    else:
        print('. perdeu todo o valor apostado!!!')