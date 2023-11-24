'''Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida 
respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade 
de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será 
o valor arrecadado.'''

print('Digite a quantidade de camisetas da venda:')
print('=' * 40)
P = float(input('Camisetas pequenas-> '))
M = float(input('Camisetas média->: '))
G = float(input('Camisetas grandes-> '))
venda = P * 10 + M * 12 + G * 15
print(f'O total arrecadado é = R${venda:.2f}')
