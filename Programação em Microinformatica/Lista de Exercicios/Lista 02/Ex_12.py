'''
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe
naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
'''
print('Informe uma data')
dia = int(input('Dia -> '))
mes = int(input('Mês -> '))
ano = int(input('Ano -> '))
valida = False
if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if 1 <= dia <= 29:
            valida = True
    else:
        if 1 <= dia <= 28:
            valida = True
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        valida = True
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        valida = True

if valida:
    print('Data válida!!')
else:
    print('Data inválida!!')
