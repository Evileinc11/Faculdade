'''Entrada
A entrada contém três linhas, cada uma com um número inteiro, P, D_1 e D_2, nesta 
ordem. Se P = 0 então Alice gritou "par", ao passo que se P=1 então Bob gritou "par". Os 
números D_1 e D_2 indicam, respectivamente, o número de dedos estendidos da Alice 
e do Bob.
Saída
Seu programa deverá imprimir uma única linha, contendo um único número inteiro, que 
deve ser 0 se Alice foi a ganhadora, ou 1 se Bob foi o ganhador'''

P = int(input('Informe qual foi o grito -> '))
d_1 = int(input('Iforme quantos dedos alice levantou -> '))
d_2 = int(input('Informe quantos dedos bob levantou -> '))
s = d_1 + d_2
if P == 0:
    if s % 2 == 0:
        print('Alice ganhou')
    else:
        print('Bob ganhou')
if P == 1:
    if s % 2 == 0:
        print('Bob ganhou')
    else:
        print('Alice ganhou')