def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
a = input('Nhap day so thuc: ')
a = [float(x) for x in a.split()]
print('Danh sach sau khi sap xep la :', insertion_sort(a))