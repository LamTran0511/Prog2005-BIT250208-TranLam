sinh_vien = {'Long':9.5,'Lâm':8.5,'Quốc':8}
tong = 0
dem = 0
for i in sinh_vien:
    tong += sinh_vien[i]
    dem += 1
print(f'Diem trung binh cua {i} sinh vien la:', tong/dem)