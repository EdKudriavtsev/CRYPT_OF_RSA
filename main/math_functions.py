def is_prime(n):
    if n <= 1:
        return False
    res = True
    k = 2
    while k * k <= n:
        if n % k == 0:
            res = False
            break
        k += 1
    return res


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a if b == 0 else b


def find_mod_inverse(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = find_mod_inverse(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def binary_search(data, x):
    L = 0
    R = len(data)
    while L < R - 1:
        c = (L + R) // 2
        if x < data[c]:
            R = c
        else:
            L = c
    return L
