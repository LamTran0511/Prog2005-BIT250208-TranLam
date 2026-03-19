import math
import matplotlib.pyplot as plt


def bai1():
    def lay_ten_file(duong_dan):
        duong_dan = duong_dan.replace("/", "\\")
        return duong_dan.split("\\")[-1]

    def lay_ten_bai_hat(duong_dan):
        ten_file = lay_ten_file(duong_dan)
        return ten_file.rsplit(".", 1)[0]

    duong_dan = input("Nhập đường dẫn file nhạc: ")
    print("Tên file:", lay_ten_file(duong_dan))
    print("Tên bài hát:", lay_ten_bai_hat(duong_dan))


def bai2():
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


def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)


def bai3():
    n = int(input("Nhập số nguyên dương: "))
    if n < 0:
        print("Không tính giai thừa cho số âm.")
    else:
        print(f"Giai thừa của {n} là: {giai_thua(n)}")


def bai4():
    chuoi = input("Nhập chuỗi: ")
    if chuoi == "":
        print("Lỗi: chuỗi rỗng.")
    else:
        print("Độ dài chuỗi là:", len(chuoi))


def bai5():
    x1 = list(range(-10, 11))
    y1 = [x ** 2 for x in x1]

    x2 = list(range(0, 11))
    y2 = [math.sqrt(x) for x in x2]

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.plot(x1, y1)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.subplot(1, 2, 2)
    plt.plot(x2, y2)
    plt.title("y = sqrt(x)")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.tight_layout()
    plt.show()


def bai6():
    chuoi = input("Nhập chuỗi: ")
    ket_qua = ""
    for i in range(len(chuoi) - 1, -1, -1):
        ket_qua += chuoi[i]
    print("Chuỗi đảo ngược là:", ket_qua)


def bai7():
    mat_khau_dung = "python123"
    mat_khau = ""
    while mat_khau != mat_khau_dung:
        mat_khau = input("Nhập mật khẩu: ")
        if mat_khau != mat_khau_dung:
            print("Sai mật khẩu, nhập lại.")
    print("Mật khẩu đúng.")


def bai8():
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


def bai9():
    class Nguoi:
        so_luong = 0

        def __init__(self, ten, tuoi):
            if ten.strip() == "":
                raise ValueError("Tên không được rỗng.")
            self.__ten = ten
            self.set_tuoi(tuoi)
            Nguoi.so_luong += 1

        def get_ten(self):
            return self.__ten

        def get_tuoi(self):
            return self.__tuoi

        def set_ten(self, ten):
            if ten.strip() == "":
                raise ValueError("Tên không hợp lệ.")
            self.__ten = ten

        def set_tuoi(self, tuoi):
            if tuoi < 0:
                raise ValueError("Tuổi phải >= 0.")
            self.__tuoi = tuoi

        def gioi_thieu(self):
            return f"Tôi là {self.__ten}, {self.__tuoi} tuổi."

        @classmethod
        def tong_so_luong(cls):
            return cls.so_luong

        @staticmethod
        def la_nguoi_lon(tuoi):
            return tuoi >= 18

        def __str__(self):
            return f"Nguoi(ten='{self.__ten}', tuoi={self.__tuoi})"

        def __eq__(self, other):
            return self.__ten == other.__ten and self.__tuoi == other.__tuoi

    class SinhVien(Nguoi):
        def __init__(self, ten, tuoi, ma_sv):
            super().__init__(ten, tuoi)
            self.__ma_sv = ma_sv

        def get_ma_sv(self):
            return self.__ma_sv

        def set_ma_sv(self, ma_sv):
            if ma_sv.strip() == "":
                raise ValueError("Mã sinh viên không được rỗng.")
            self.__ma_sv = ma_sv

        def hoc_bai(self):
            return f"Sinh viên {self.get_ten()} đang học bài."

        def __str__(self):
            return f"SinhVien(ten='{self.get_ten()}', tuoi={self.get_tuoi()}, ma_sv='{self.__ma_sv}')"

        def __eq__(self, other):
            return self.__ma_sv == other.__ma_sv

    n1 = Nguoi("An", 20)
    n2 = Nguoi("An", 20)
    sv1 = SinhVien("Bình", 19, "SV01")
    sv3 = SinhVien("Bình", 22, "SV01")

    print("Getter:")
    print(n1.get_ten())
    print(n1.get_tuoi())

    print("\nSetter:")
    n1.set_ten("An Nguyễn")
    n1.set_tuoi(22)
    print(n1)

    print("\nPhương thức đối tượng:")
    print(n1.gioi_thieu())
    print(sv1.hoc_bai())

    print("\nPhương thức lớp:")
    print("Tổng số đối tượng:", Nguoi.tong_so_luong())

    print("\nStatic method:")
    print("20 có phải người lớn không?", Nguoi.la_nguoi_lon(20))

    print("\n__str__:")
    print(n1)
    print(sv1)

    print("\nNạp chồng toán tử == :")
    print("n1 == n2:", n1 == n2)
    print("sv1 == sv3:", sv1 == sv3)

    print("\nKế thừa:")
    print(sv1.gioi_thieu())


while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("8. Bài 8")
    print("9. Bài 9")
    print("10. Bài 10")
    print("0. Thoát")

    chon = input("Nhập lựa chọn: ")

    if chon == "1":
        bai1()
    elif chon == "2":
        bai2()
    elif chon == "3":
        bai3()
    elif chon == "4":
        bai4()
    elif chon == "5":
        bai5()
    elif chon == "6":
        bai6()
    elif chon == "7":
        bai7()
    elif chon == "8":
        bai8()
    elif chon == "9":
        bai9()
    elif chon == "10":
        bai8()
    elif chon == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")
