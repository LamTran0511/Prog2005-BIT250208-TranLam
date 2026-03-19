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
sv2 = SinhVien("Cường", 21, "SV02")
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

print("\nTest ValueError:")
try:
    x = Nguoi("", 10)
except ValueError as e:
    print("Lỗi 1:", e)

try:
    y = Nguoi("Lan", -5)
except ValueError as e:
    print("Lỗi 2:", e)