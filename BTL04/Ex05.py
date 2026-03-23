my_dict = {}

while True:
    try:
        n = int(input("Nhập số lượng phần tử: "))
        if n <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

for i in range(n):
    key = input(f"Nhập key thứ {i + 1}: ")
    value = input(f"Nhập value thứ {i + 1}: ")
    my_dict[key] = value

print("Dictionary hiện tại:", my_dict)

k = input("Nhập key cần kiểm tra: ")

if k in my_dict:
    print(f'Key "{k}" có tồn tại trong dictionary')
else:
    print(f'Key "{k}" không tồn tại trong dictionary')