for i in range (100, 1000):
    num = i
    c = num // 100
    d = num % 100 // 10
    u = num % 10
    if i % 2 == 0:
        soma = c + d + u
        print(f'A variavel {i} -> {soma}')
    else:
        mult = c * d * u
        print(f'A variavel {i} -> {mult}')

