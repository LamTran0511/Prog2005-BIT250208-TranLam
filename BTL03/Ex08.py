ds = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    ds.append(s)

print("Danh sách ban đầu:", ds)

buoc = 1
for i in range(len(ds) - 1):
    for j in range(len(ds) - 1 - i):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
            print(f"Bước {buoc}: {ds}")
            buoc += 1

print("Kết quả cuối cùng:", ds)