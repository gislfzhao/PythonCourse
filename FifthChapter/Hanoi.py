# Hanoi

count = 0


def hanoi(n, left="left", right="right", mid="mid"):
    global count
    if n == 1:
        print("{},{}->{}".format(n, left, right))
    else:
        hanoi(n - 1, left, mid, right)
        print("{},{}->{}".format(n, left, right))
        count += 1
        hanoi(n - 1, mid, right, left)


if __name__ == "__main__":
    hanoi(3)
