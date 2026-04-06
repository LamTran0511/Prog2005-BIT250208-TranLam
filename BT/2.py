import math
ds = []
so_le = []
tong = 0
SNT = []
a = int(input('nhap so luong mang: '))
for i in range(a):
    n = int(input(f'nhap phan tu thu {i}: '))
    ds.append(n)
for x in ds:
    if x % 2 != 0:
        so_le.append(x)
for b in so_le:
    tong += b
print('ds so le la: ', so_le)
print('tong le la: ', tong)

for c in ds:
    if c < 2:
        continue
    la_snt = True
    for d in range(2, int(math.sqrt(c)) + 1):
        if c % d == 0:
            la_snt = False
            break
    if la_snt:
        SNT.append(c)

print('ds cac snt la ', SNT)