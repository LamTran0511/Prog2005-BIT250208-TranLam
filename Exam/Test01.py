from math import trunc


def bai01():
    a = int(input('Nhập số nguyên a: '))
    b = int(input('Nhập số nguyên b: '))
    c = int(input('Nhập số nguyên c: '))
    max_value = max(a, b, c)
    min_value = min(a, b, c)
    print('Số lớn nhất là: ',max_value)
    print('Số bé nhất là: ',min_value)
    print(f'Phương trình bậc 2 là: {a}x^2 + {b}x + {c} = 0')

    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            x = -c / b
            print("Phương trình có nghiệm x =", x)
    else:
        print("Đây là phương trình bậc 2")

def bai02():
    def selection_sort(a):
        n = len(a)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if a[j] > a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a

    a = []
    for i in range(16, 112):
        if i % 2 != 0:
            a.append(i)
    print('Dãy số lẻ là: ', selection_sort(a))

    a = []
    for i in range(16, 112):
        for j in range(i+1, 112):
            if i % 2 == 0:
                a.append(i)
    print('Đây là số nguyên tố: ', selection_sort(a))

def bai03():
    n = int(input('Nhập n: '))
    print('Hình 1:')
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    print('Hình 2: ')
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("* ", end=' ')
        print()

def bai04():
    n = int(input("Nhập số phần tử N: "))
    a = []

    for i in range(n):
        x = int(input(f"Nhập phần tử a[{i}]: "))
        a.append(x)

    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if a[j] > a[max_index]:
                max_index = j

        a[i], a[max_index] = a[max_index], a[i]

        print(f"Sau bước {i + 1}:", end=" ")
        print(*a)
while True:
    print("\n******************MENU******************")
    print('1.Bài 1.')
    print('2.Bài 2.')
    print('3.Bài 3.')
    print('4.Bài 4.')
    print('5.Thoát.')
    choice = int(input('Chọn bài: '))
    if choice == 1:
        bai01()
    elif choice == 2:
        bai02()
    elif choice == 3:
        bai03()
    elif choice == 4:
        bai04()
    elif choice == 5:
        print('Chương trình đã kết thúc.')
        break
    else:
        print('Lỗi thao tác không có trong menu')
