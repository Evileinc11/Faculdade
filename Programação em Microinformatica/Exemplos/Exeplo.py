M = [0] * 3
for i in range(3):
    M[i] = [0] * 4
    for j in range(4):
        M[i][j] = int(input(f'[{i}{j}]-> '))

M = []
for i in range(3):
    M.append([])
    for j in range(4):
        M[i].append(int(input(f'[{i}{j}]-> ')))

for i in range(3):
    for j in range(4):
        print(f'{M[i][j]:2}',end=' ')
    print()