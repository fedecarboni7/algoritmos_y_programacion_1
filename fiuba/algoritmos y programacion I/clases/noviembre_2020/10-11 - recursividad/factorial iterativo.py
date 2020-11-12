def factorial_iterativo(n):
    res = 1
    if n >= 2:
        for i in range(n, 0, -1):
            res *= i
    return res
