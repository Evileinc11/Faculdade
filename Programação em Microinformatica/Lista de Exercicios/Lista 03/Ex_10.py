'''
Faça um programa para ler 2 valores, calcular e escrever a
soma dos inteiros existentes entre os 2 valores lidos
(incluindo os valores lidos na soma). O programa deve validar
que o 1º valor informado seja menor que o 2º valor.
O programa deve permitir que o usuário possa executá-lo novamente.
'''

while True:
    print("Informe o intervalo...")
    ini = int(input("Início -> "))
    fim = int(input("Fim -> "))
    if ini > fim:
        ini, fim = fim, ini
    soma = 0
    for n in range(ini, fim+1):
        soma += n
    print(f"A soma dos valores entre {ini} e {fim} é {soma}")
    resp = input("Deseja entrar com outro intervalo? [S/N] -> ").upper()[0]
    print('~' * 45)
    if resp != 'S':
        break