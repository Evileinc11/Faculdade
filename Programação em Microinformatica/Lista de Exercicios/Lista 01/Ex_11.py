'''Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um 
programa para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que 
Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos, 
R$33,00 para André e R$35,53 para Felipe'''

conta = float(input('Informe o valor da compra -> R$ '))
reais = int(conta)
centavos = conta - reais
ca = reais // 3
f = conta - (ca*2)
print(f'Divisão da conta:\nCarlos -> R$ {ca:.2f}\nAndré -> R$ {ca:.2f}\nFelipe -> R$ {f:.2f}')
