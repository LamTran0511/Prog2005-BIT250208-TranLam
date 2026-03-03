def count_vowels(s):
    vowels = "aeiou"
    s = s.lower()
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count
n = input('Nhap chuoi :')
print('So luong nguyen am la : ', count_vowels(n))