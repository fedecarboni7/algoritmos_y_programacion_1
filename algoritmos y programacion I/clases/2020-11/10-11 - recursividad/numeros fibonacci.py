def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

# aplicando mnemoization
cache = {0: 1, 1: 1}

def fib_m(n):
    if n not in cache:
        cache[n] = fib_m(n-1) + fib_m(n-2)
    return cache[n]
