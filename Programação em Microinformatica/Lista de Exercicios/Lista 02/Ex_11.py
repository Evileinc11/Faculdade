'''
Leia a distância em Km e a quantidade de litros de gasolina consumidos por
um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
acordo com a tabela abaixo:
Consumo	Km/l	Mensagem
Menor que	8	Venda o carro
Entre	8 e 14	Econômico
Maior que	14 	Super econômico
'''
distancia = float(input("Informe a distância percorrida -> "))
litros = float(input("Informe quantos litros de combustível usou -> "))
consumo = distancia / litros
print(f"Seu veículo faz {consumo:.2f} km/l")
if consumo < 8:
    print("Venda o carro!!")
elif consumo <= 14:
    print("Econômico!!")
else:
    print("Super econômico")
