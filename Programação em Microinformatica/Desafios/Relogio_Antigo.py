'''
Entrada
A entrada consiste em dois valores inteiros h e m que são, respectivamente, os ângulos 
medidos sobre os ponteiros de hora e de minuto.
Saída
Imprima uma única linha com o valor da hora e do minuto no formato "hh:mm" (sem 
aspas), conforme pode ser observado nos exemplos'''

h = int(input('Informe os graus equivalente a hora -> '))
m = int(input('Informe os graus equivalente a minuto -> '))
hora = h // 30
min = m // 6
print(f'Hora = {hora:02}:{min:02}')

#360/12 = 30°
#360/60 = 6°