'''Faça um programa que peça a distância a ser percorrida e a velocidade média do veículo. Calcule e 
imprima quanto tempo levará o veículo para percorrer a distância. Mostre em horas, minutos.
Exemplo:
Distância = 165 km
Velocidade = 110 km/h
Tempo = 1,5
Exibir 1 hora e 30 minutos'''

distancia = float(input('Informe a distância a ser percorrida -> '))
velocidade = float(input('Qual a velocidade média do veículo? -> '))
horas = distancia / velocidade
h = int(horas)
m = int((horas - h) * 60)
print(f'Levará ({horas:.2f}) {h} horas e {m} minutos para percorrer essa distância a essa velocidade')