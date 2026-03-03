data = input('Nhap danh sach so cua ban : ')
arr = [int(x) for x in data.split()]
GTLN = arr[0]
GTNN = arr[0]
for i in arr:
    if i > GTLN:
        GTLN = i
    if i < GTNN:
        GTNN = i
print('GTLN la: ', GTLN)
print('GTNN la: ', GTNN)