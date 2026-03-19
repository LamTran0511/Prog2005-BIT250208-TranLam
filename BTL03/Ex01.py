def lay_ten_file(duong_dan):
    duong_dan = duong_dan.replace("/", "\\")
    return duong_dan.split("\\")[-1]

def lay_ten_bai_hat(duong_dan):
    ten_file = lay_ten_file(duong_dan)
    return ten_file.rsplit(".", 1)[0]

duong_dan = "d:\\music\\muabui.mp3"
print("Tên file:", lay_ten_file(duong_dan))
print("Tên bài hát:", lay_ten_bai_hat(duong_dan))