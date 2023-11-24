num = int(input('Digite um número -> '))
soma = 0
imp = 1
while soma < num:
    print(imp, end='+')
    soma += imp
    imp += 2
if soma == num:
    print(num,'é quadrado perfeito!')
else:
    print(num,'não é')
