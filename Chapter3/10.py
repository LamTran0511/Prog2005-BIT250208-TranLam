n = input('Nhap danh sach so cua ban: ')
a = [float(arr) for arr in n.split()]
b = [arr for arr in a if arr %2 == 0]
tong = 0
print('Danh sach so chan trong day so la : ', b)
for i in b:
    tong += i
print('Tong cac so chan la ', tong)