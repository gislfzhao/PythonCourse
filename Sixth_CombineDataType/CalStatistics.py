# Calculate Statistics


def get_num():
    numbers = []
    num_str = input("请输入数字(回车退出)：")
    while num_str != "":
        numbers.append(eval(num_str))
        num_str = input("请输入数字(回车退出)：")
    return numbers


def mean(numbers):
    num_sum = 0.0
    for num in numbers:
        num_sum += num
    return num_sum / len(numbers)


def dev(numbers, mean):
    num_dev = 0.0
    for num in numbers:
        num_dev += pow(num - mean, 2)
    return num_dev / len(numbers)


def median(numbers):
    num_len = len(numbers)
    numbers.sort()
    if num_len % 2 == 0:
        return (numbers[num_len // 2] + numbers[num_len // 2 - 1]) / 2
    else:
        return numbers[num_len // 2]


def sort(numbers):
    numbers.sort()
    print("正向排序如下：")
    for num in numbers:
        print(num, end=",")
    print("\b")


if __name__ == "__main__":
    nums = get_num()
    sort(nums)
    m = mean(nums)
    print("平均值：{:.2f},方差：{:.4},中位数：{}." .format(m, dev(nums, m), median(nums)))
