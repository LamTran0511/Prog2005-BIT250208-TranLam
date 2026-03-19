chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập 1 ký tự: ")

if len(ky_tu) != 1:
    print("Lỗi: chỉ được nhập 1 ký tự.")
else:
    dem = 0
    for i in chuoi:
        if i == ky_tu:
            dem += 1
    print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần.")