def khoa_sap_xep(s):
    return (-len(s), s)

def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and khoa_sap_xep(arr[j]) > khoa_sap_xep(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search_strings(arr, target):
    left = 0
    right = len(arr) - 1
    target_key = khoa_sap_xep(target)

    while left <= right:
        mid = (left + right) // 2
        mid_key = khoa_sap_xep(arr[mid])

        if mid_key == target_key and arr[mid] == target:
            return mid
        elif target_key < mid_key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


ds = []
print("Nhập 5 chuỗi:")
for i in range(5):
    s = input(f"Chuỗi thứ {i + 1}: ")
    ds.append(s)

insertion_sort_strings(ds)
print("\nDanh sách sau khi sắp xếp:")
for i, s in enumerate(ds, start=1):
    print(f"Vị trí {i}: {s}")

x = input("\nNhập chuỗi cần tìm: ")
vi_tri = binary_search_strings(ds, x)

if vi_tri != -1:
    print(f'Tìm thấy "{x}" ở vị trí {vi_tri + 1}')
else:
    print(f'Không tìm thấy "{x}" trong danh sách')