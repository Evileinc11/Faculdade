n = int(input('Informe a altura -> '))

for i in range(1,2*n,2):
    linha = ''
    for j in range(i):
        linha += '*'
    print(linha.center(2*n))
