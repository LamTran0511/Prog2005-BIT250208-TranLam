m = int(input('So hang : '))
n = int(input('So cot : '))
print('Ma Tran A ')
A = []
for i in range(m):
    row = [float(x) for x in input().split()]
    A.append(row)
print('Ma Tran B')
B = []
for i in range(m):
    row = [float(x) for x in input().split()]
    B.append(row)
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print('Tong 2 ma tran la : ')
for row in C:
    print(row)