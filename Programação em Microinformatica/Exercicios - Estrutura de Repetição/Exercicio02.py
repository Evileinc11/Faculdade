n = int(input('Informe a altura -> '))

for i in range(1,n):
    for j in range(i):
        print('*', end='')
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print("=" * 50)

for i in range(1,2*n):
    if i < n:
        for j in range(i):
            print('*', end='')
    else:
        for j in range(2*n-i):
            print('*', end='')
    print()
