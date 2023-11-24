'''Implemente um programa para ler o preço do litro do combustível de um carro, ler o desempenho 
do veículo (km/l) e a distância entre duas cidades (km), e informar quantos litros, e quanto dinheiro 
vai ser gasto para fazer uma viagem entre as duas cidades.'''

L = float(input('Digite o preço do litro do combustivel: '))
D = float(input('Digite a distância: '))
V = float(input('Quantidade de quilometros feito por litros: '))
Lc = D / V
Pr = Lc * L
print(f'A quantidade de litros gastos será -> {Lc:.2f} , e o valor gasto será -> R$ {Pr:.2f}')