mausac = ['Blue','Red','Pink','Black']
try :
    mausac.remove('Green')
    print(mausac)
except ValueError :
    print('Khong co mau Green')
print('Danh sach mau sac la :', mausac)