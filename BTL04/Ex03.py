def bai03():
    while True:
        du_lieu = input("Nhập danh sách số nguyên, cách nhau bởi dấu cách: ")
        if du_lieu == "":
            print("Không được để trống!")
            continue

        try:
            ds = list(map(int, du_lieu.split()))
            break
        except ValueError:
            print("Vui lòng nhập đúng các số nguyên!")

    so_chan = []
    tong_chan = 0

    for i in ds:
        if i % 2 == 0:
            so_chan.append(i)
            tong_chan += i

    print(f"Số chẵn là: {so_chan}")
    print(f"Tổng các số chẵn là: {tong_chan}")


bai03()