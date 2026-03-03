n = input('Nhap danh sach so cua ban: ')
a = [float(arr)for arr in n.split()]
for i in a:
    if i > 10:
        print(f'So dau tien lon hon 10 la: {i} ')
        break
    else:
        print('Khong co so nao lon hon 10')
        break
        