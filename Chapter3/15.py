def cach1():
    n = input('Nhap chuoi : ')
    reverse_n = n[::-1]
    print('Dung slicing: ', reverse_n)
cach1()
def cach2():
    n = input('Nhap chuoi : ')
    reverse_n = ""
    for ch in n:
        reverse_n = ch + reverse_n
    print('Khong dung slicing', reverse_n)
cach2()