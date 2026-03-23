def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    du_lieu = input("Nhập danh sách số nguyên ban đầu, cách nhau bởi dấu cách: ").strip()
    if du_lieu == "":
        print("Không được để trống, vui lòng nhập lại!")
        continue

    try:
        ds = list(map(int, du_lieu.split()))
        break
    except ValueError:
        print("Dữ liệu không hợp lệ, vui lòng nhập lại!")

print("Danh sách ban đầu:", ds)

while True:
    try:
        x = int(input("Nhập phần tử cần thêm vào danh sách: "))
        ds.append(x)
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

print("Danh sách sau khi thêm:", ds)

while True:
    try:
        k = int(input("Nhập giá trị k cần kiểm tra số lần xuất hiện: "))
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

print(f"Số lần xuất hiện của {k} là: {ds.count(k)}")

tong_nguyen_to = sum(x for x in ds if la_so_nguyen_to(x))
print("Tổng các số nguyên tố trong danh sách là:", tong_nguyen_to)

ds.sort()
print("Danh sách sau khi sắp xếp tăng dần:", ds)

ds.clear()
print("Danh sách sau khi xóa:", ds)