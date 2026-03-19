mat_khau_dung = "123456"
mat_khau = ""

while mat_khau != mat_khau_dung:
    mat_khau = input("Nhập mật khẩu: ")
    if mat_khau != mat_khau_dung:
        print("Sai mật khẩu, nhập lại.")

print("Mật khẩu đúng.")