import csv

nhan_vien_list = []

while True:
    try:
        n = int(input("Nhập số lượng nhân viên: "))
        if n <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

for i in range(n):
    print(f"\n--- Nhập thông tin nhân viên thứ {i + 1} ---")
    ma_nv = input("Nhập ID: ").strip()
    ten_nv = input("Nhập tên: ").strip()

    while True:
        try:
            tuoi_nv = int(input("Nhập tuổi: "))
            if tuoi_nv < 0:
                print("Tuổi không được âm!")
                continue
            break
        except ValueError:
            print("Tuổi phải là số nguyên!")

    nhan_vien_list.append({
        "id": ma_nv,
        "ten": ten_nv,
        "tuoi": tuoi_nv
    })

ten_file_txt = "nhanvien.txt"
with open(ten_file_txt, "w", encoding="utf-8") as f:
    f.write("DANH SÁCH NHÂN VIÊN\n")
    for nv in nhan_vien_list:
        f.write(f"ID: {nv['id']} | Tên: {nv['ten']} | Tuổi: {nv['tuoi']}\n")

ten_file_csv = "nhanvien.csv"
with open(ten_file_csv, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Tuổi"])
    for nv in nhan_vien_list:
        writer.writerow([nv["id"], nv["ten"], nv["tuoi"]])
print(f"\nĐã lưu vào file text: {ten_file_txt}")
print(f"Đã lưu vào file csv: {ten_file_csv}")
print("\n--- Nội dung file TXT ---")
with open(ten_file_txt, "r", encoding="utf-8") as f:
    print(f.read())
print("--- Nội dung file CSV ---")
with open(ten_file_csv, "r", encoding="utf-8-sig") as f:
    print(f.read())