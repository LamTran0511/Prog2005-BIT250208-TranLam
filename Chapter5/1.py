import matplotlib.pyplot as plt

Danh_hieu = ['XS', 'G', 'TB', 'Y','K']
So_luong = [6,10,12,4,1]

plt.bar(Danh_hieu, So_luong, color='blue')
plt.title('KET QUA HOC TAP')
plt.xlabel('Danh hieu')
plt.ylabel('So luong')
plt.figure(figsize=(10,5))
plt.show()