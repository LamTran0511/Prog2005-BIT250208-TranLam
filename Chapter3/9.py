n = input('Nhap day so cua ban: ')
a = [float(arr) for arr in n.split()]
b = [x for x in a if x % 2 != 0]
print('Danh sach so le trong day so la: ', b)