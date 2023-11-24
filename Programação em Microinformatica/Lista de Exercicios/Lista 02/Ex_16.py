'''
12.	Bits Trocados
As Ilhas Weblands formam um reino independente nos mares do Pacífico.
Como é um reino recente, a sociedade é muito influenciada pela informática.
A moeda oficial é o Bit; existem notas de B$ 50,00, B$10,00, B$5,00 e B$1,00.
Você foi contratado(a) para ajudar na programação dos caixas automáticos de um
grande banco das Ilhas Weblands.

Tarefa
Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas
disponíveis, mantendo um estoque de cédulas para cada valor
(B$ 50,00, B$10,00, B$5,00 e B$1,00). Os clientes do banco utilizam os caixas
eletrônicos para efetuar retiradas de um certo número inteiro de Bits.
Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo
cliente, determine o número de cada uma das notas necessário para totalizar esse
valor, de modo a minimizar a quantidade de cédulas entregues. Por exemplo,
se o cliente deseja retirar B$50,00, basta entregar uma única nota de cinquenta Bits.
Se o cliente deseja retirar B$72,00, é necessário entregar uma nota de B$50,00,
duas de B$10,00 e duas de B$1,00.
'''

valor = int(input("Informe o valor em B$ -> "))
n50 = valor // 50
n10 = valor % 50 // 10
n5 = valor % 50 % 10 // 5
n1 = valor % 5
print("Cédulas entregues:")
if n50 > 0:
    print(f"{n50} notas de B$ 50,00")
if n10 > 0:
    print(f"{n10} notas de B$ 10,00")
if n5 > 0:
    print(f"{n5} notas de B$ 5,00")
if n1 > 0:
    print(f"{n1} notas de B$ 1,00")







