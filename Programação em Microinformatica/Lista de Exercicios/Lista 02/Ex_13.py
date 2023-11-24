''' Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de leite 
(estes dados são constantes nesta receita). Você deve escrever um programa em Python que dados 
como entrada A (quantidade de xicaras de farinha de trigo), B (quantidade de ovos) e C (quantidade 
de colheres de leite) todos valores inteiros, o programa deve mostrar quantos bolos podem ser 
produzidos. 
Veja a simulação: 
Ex.1 A = 4 B = 6 e C = 10 ➔ produzirá a saída: 2 bolos. 
Ex.2 A = 4 B = 6 e C = 9 ➔ produzirá a saída: 1 bolo. 
Ex.3 A = 10 B = 10 e C = 25 ➔ produzirá a saída: 3 bolos.'''

print('Informe a quantidade de ingredientes que você tem de:')

farinha = int(input('Xícaras de farinha -> '))
ovo = int(input('Ovos -> '))
leite = int(input('Colheres de leite -> '))

A = farinha // 2
B = ovo // 3
C = leite // 5
print(f'Com a quantidade de farinha, é possivel fazer {A} bolo(s)')
print(f'Com a quantidade de ovos, é possivel fazer {B} bolo(s)')
print(f'Com a quantidade de leite, é possivel fazer {C} bolo(s)')
if A <= B and A <= C:
    print(f'Você fará {A} bolo(s)')
elif B <= C:
    print(f'Você fará {B} bolo(s)')
else:
    print(f'Você fará {C} bolo(s)')