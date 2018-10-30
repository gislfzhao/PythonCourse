# Fibonacci Numbers


def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    for i in range(1, 100):
        print(i, fibo(i))
