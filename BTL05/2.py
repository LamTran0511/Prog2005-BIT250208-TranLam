n = input('nhap chuoi: ')
a = 0
dem = 0
for i in n:
    a += 1
for j in n:
    if j == 'a':
        dem += 1
print('do dai',a)
print('so lan xuat hien chu a la: ', dem)