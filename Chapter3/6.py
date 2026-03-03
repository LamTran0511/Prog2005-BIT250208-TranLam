dem = 0
def bubble_sort(arr):
    n = len(arr)
    global dem
    for i in range(0, n):
        doi_cho = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                dem += 1
                doi_cho = True
        if not doi_cho:
            break
    return arr
a = [10,9,8,7,6,5,4,3,2,1]
print('Danh sach sau khi sap xep la: ', bubble_sort(a))
print('So lan hoan doi la: ', dem)