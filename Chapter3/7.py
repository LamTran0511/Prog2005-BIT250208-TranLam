def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n = input('Nhap danh sach cua ban : ')
arr = [float(num) for num in n.split()]
x = float(input('Nhap so can tim'))
a = linear_search(arr, x)
if a != -1:
    print(f'So {x} duoc tim thay tai chi so {a}')
else:
    print(f'Khong co so {x}')