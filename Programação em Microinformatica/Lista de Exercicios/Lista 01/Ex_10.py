'''Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um programa
para converter este tempo em anos, meses e dias. Assuma que cada ano possui sempre 365 dias e 
que cada mês possui sempre 30 dias. Exemplo: 1451 dias são 3 anos, 11 meses e 26 dias'''

dias = int(input('Informe a quantidade de dias que a fábrica está sem acidentes -> '))
a = dias // 365
m = dias % 365 // 30
d = dias % 365 % 30
print(f'A fábrica está há {a} anos, {m} meses e {d} dias sem acidentes!!')
