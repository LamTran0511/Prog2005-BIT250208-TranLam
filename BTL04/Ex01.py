def insertion_sort(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        print(f"Lấy '{key}' làm key")
        j = i - 1
        while j >= 0 and len(strings[j]) < len(key):   # giảm dần theo độ dài
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
        print(f"Chèn key vào vị trí đúng: {strings}")
    return strings

arr = []
for i in range(1, 6):
    n = input(f"Nhập chuỗi thứ {i}: ")
    arr.append(n)
print("Kết quả sau sắp xếp:", insertion_sort(arr))