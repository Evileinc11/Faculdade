'''Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um programa para ler o preço 
do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.'''

V = float(input('Digite o valor que deseja abastecer: '))
G = float(input('Digite o preço do litro da gasolina: '))
L = V/G
print(f'O total de litros será -> {L:.2f}')