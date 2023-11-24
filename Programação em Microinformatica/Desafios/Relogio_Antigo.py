h = int(input('Informe os graus equivalente a hora -> '))
m = int(input('Informe os graus equivalente a minuto -> '))
hora = h // 30
min = m // 6
print(f'Hora = {hora:02}:{min:02}')

#360/12 = 30°
#360/60 = 6°