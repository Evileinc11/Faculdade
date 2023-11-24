'''
Quadrante
Leia 2 valores com casa decimal (x e y), que devem representar as coordenadas de um ponto em um 
plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos 
cartesianos ou na origem (x = y = 0)
'''
print('Entre com a coordenada do ponto')
x = float(input('x >> '))
y = float(input('y >> '))
if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo y')
elif y == 0:
    print('Eixo x')
elif x > 0 and y > 0:
    print('Quadrante 1')
elif x < 0 and y > 0:
    print('Quadrante 2')
elif x < 0 and y < 0:
    print('Quadrante 3')
else:
    print('Quadrante 4')
