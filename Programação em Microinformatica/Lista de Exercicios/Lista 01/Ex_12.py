'''Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar. Faça 
um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, 
em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. Não 
havendo moeda de um tipo, a quantidade respectiva é zero'''

print('Pedrinho, informe a quantidade de moedas que tem no cofrinho')
m1c = int(input('R$ 0,01 -> '))
m5c = int(input('R$ 0,05 -> '))
m10c = int(input('R$ 0,10 -> '))
m25c = int(input('R$ 0,25 -> '))
m50c = int(input('R$ 0,50 -> '))
m1r = int(input('R$ 1,00 -> '))
total = m1c*0.01 + m5c*0.05 + m10c*0.10 + m25c*0.25 + m50c*0.5 + m1r
print(f"Você tem R$ {total:.2f} no seu cofrinho!!")