Dic = {'Long':'25IT','Lâm':'25IT','Quốc':'25IT','Khải':'25MK'}
a = input('Nhap key: ')
if a not in Dic:
    print('Key nay khong ton tai trong dictionary')
else:
    print(Dic[a])