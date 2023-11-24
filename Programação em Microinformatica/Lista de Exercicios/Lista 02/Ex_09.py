'''
A nota ﬁnal de um estudante é calculada a partir de três notas atribuídas
entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório,
a uma avaliação semestral e a um exame ﬁnal. A média das três notas mencionadas
anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3;
Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado
(média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado.
Faça todas as veriﬁcacões necessárias.
'''
print("Informe as notas do aluno")
TL = float(input("Nota de trabalho de laboratório -> "))
AS = float(input("Nota de avaliação semestral -> "))
EF = float(input("Nota de exame final -> "))
if 0 <= TL <= 10 and 0 <= AS <= 10 and 0 <= EF <= 10:
    media = (TL*2 + AS*3 + EF*5) / 10
    if media < 3:
        print(f"Aluno REPROVADO com média igual a {media:.2f}")
    elif media < 5:
        print(f"Aluno de RECUPERAÇÃO com média igual a {media:.2f}")
    else:
        print(f"Aluno APROVADO com média igual a {media:.2f}")
else:
    print("Alguma nota inválida!!!")
