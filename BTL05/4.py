def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
n = int(input('nhap n: '))
print(f'{n}!= ',factorial(n))
