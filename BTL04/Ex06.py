def selection_sort_dict_giam_dan_theo_tuoi(d):
    items = list(d.items())
    n = len(items)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if items[j][1] > items[max_idx][1]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
    return dict(items)

thong_tin = {}
while True:
    try:
        n = int(input("Nhập số lượng người: "))
        if n <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")

for i in range(n):
    ten = input(f"Nhập tên người thứ {i + 1}: ").strip()
    while True:
        try:
            tuoi = int(input(f"Nhập tuổi của {ten}: "))
            if tuoi < 0:
                print("Tuổi không được âm!")
                continue
            break
        except ValueError:
            print("Tuổi phải là số nguyên!")
    thong_tin[ten] = tuoi

print("\nDictionary ban đầu:")
print(thong_tin)
tuoi_tb = sum(thong_tin.values()) / len(thong_tin)
print(f"Tuổi trung bình là: {tuoi_tb:.2f}")
dict_da_sap_xep = selection_sort_dict_giam_dan_theo_tuoi(thong_tin)
print("\nDictionary sau khi sắp xếp tuổi giảm dần:")
for ten, tuoi in dict_da_sap_xep.items():
    print(f"{ten}: {tuoi}")