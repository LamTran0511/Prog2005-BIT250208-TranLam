tuple = (1,2,3)
tong = 0
for i in tuple:
    tong += i
    max_idx = tuple[0]
    min_idx = tuple[0]
    if i > max_idx:
        max_idx = i
    if i < min_idx:
        min_idx = i
print('Tong la: ',tong)
print('Min la: ',min_idx)
print('Max la: ',max_idx)