'''Primeiramente o programa deve pedir ao usuário o valor do “lado” do quadrado (dimensão da matriz, sendo superior a 2 – ordem N) e então calcular o valor que deverá ser a soma das linhas, colunas e diagonais.

A fórmula pode ser calculada de duas formas:

1ª Soma-se todos os dígitos a serem inseridos, exemplo para uma matriz de lado 3, serão inseridos dígitos de 1 a 9 sendo que a soma dos mesmos é igual a 45. Divide-se este número por 3, temos que a somatória deverá ser 15.

2ª Utilizando-se a fórmula S = (n + n3) / 2, sendo n o “lado” do quadrado e maior que dois.

Assim, para o quadrado (3 por 3), a somatória é obtida da seguinte forma:

S = (3 + 33) / 2 = 15

Em seguida, terá de pedir os números de 1 a 9 em 9 casas, considerando a matriz de ordem N == 3, verificando se a soma das linhas, colunas e diagonais sejam iguais a 15, no exemplo.

Imprimir a matriz seguida da mensagem: “Quadrado Mágico” ou “Não é um Quadrado Mágico”.'''

SS = 0
SP = 0
Q = True
n = int(input('Informe a dimensão da matriz -> '))
if n > 2:
    M = [0] * n
    for i in range(n):
        M[i] = [0] * n
        for j in range(n):
            M[i][j] = int(input(f'[{i}{j}]-> '))
    s = (n + n ** 3) / 2
    for i in range(n):
        SP += M[i][i]
        SS += M[i][(n - 1) - i]
    for i in range(n):
        sl = 0
        sc = 0
        for j in range(n):
            sl += M[i][j]
            sc += M[j][i]

        if (sl != s) or (sc != s):
            Q = False

    if (SP != s) or (SS != s):
        Q = False

    print('¨' * 40)
    print('A Matriz:')

    for i in range(n):
        for j in range(n):
            print(f'{M[i][j]:02}', end=' ')
        print()

    if Q:
        print('É um quadrado mágico!')
    else:
        print('Não é um quadrado mágico!')
else:
    print('Número inválido!')