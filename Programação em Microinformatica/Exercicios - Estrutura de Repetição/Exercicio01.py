n = int(input('Informe a altura -> '))

for i in range(1,n+1):
    for j in range(i):
        print('!', end='')
    print()

print('=' * 50)

for i in range(1,n+1):
    print('!' * i)