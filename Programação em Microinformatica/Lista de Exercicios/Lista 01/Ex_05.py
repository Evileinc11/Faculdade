'''Faça um programa para ler três notas de um aluno em uma disciplina e imprimir a sua média 
ponderada (as notas têm pesos respectivos de 1, 2 e 3).'''

N1 = float(input('Digite a primeira nota -> '))
N2 = float(input('Digite a segunda nota -> '))
N3 = float(input('Digite a terceira nota -> '))
med = (N1 * 1) + (N2 * 2) + (N3 * 3) / 6
print('A sua média ponderada é = ', med)
