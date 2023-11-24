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