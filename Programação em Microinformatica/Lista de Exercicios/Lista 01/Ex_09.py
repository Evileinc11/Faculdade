'''Escreva um programa para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida ela 
possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma pessoa com 19 
anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS.
'''

nome = input('Informe o nome -> ').upper()
idade = int(input('Informe sua idade -> '))
print(f'{nome}, Você já viveu {idade*365} DIAS')