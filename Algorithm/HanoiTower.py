# Hanoi Tower
def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        # 将height - 1 从左边移动到中间
        hanoi(height - 1, left, middle, right)
        # 将最大圆盘从左边移动到右边
        print(left, "->", right)
        # 将height - 1 从中间移动到右边
        hanoi(height - 1, middle, right, left)


def hanoi2(height, left='left', right='right', middle='middle'):
    if height == 0:
        return 0
    elif height > 0:
        return hanoi2(height - 1, left, middle, right) + 1 + hanoi2(height - 1, middle, right, left)


hanoi(3)
print(hanoi2(3))
