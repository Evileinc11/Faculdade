'''
Jogo Caça Níqueis
Dados de entrada: Valor da aposta em reais.
	
O programa deverá sortear três números aleatórios (1 a 99)
e as seguintes regras deverão ser consideradas:
Se nenhum número for igual, o apostador perde o jogo,
se dois números forem iguais, o apostador ganhará 5 vezes o valor da aposta,
se acertar os três ganhará 100 vezes o valor da aposta.
Imprimir o valor ganho pelo apostador.
'''

from random import randint
print("J O G O - C A Ç A - N Í Q U E I S")
valorAposta = float(input("Informe a sua aposta-> "))
a = randint(1,99)
b = randint(1,99)
c = randint(1,99)
print(f"\nOs números sorteados foram {a} - {b} - {c}\n")
if a==b==c:
    print(f"Que sorte a sua, sairam 3 números iguais!! Você ganhou 100 x o valor apostado -> R$ {valorAposta*100:.2f}")
elif a==b or b==c or a==c:
    print(f"Parabéns!! Sairam 2 números iguais, você ganhou 5 x o valor apostado -> R$ {valorAposta*5:.2f}")
else:
    print("Infelizmente não saiu nenhum número igual!! Perdeu o valor apostado :(")
