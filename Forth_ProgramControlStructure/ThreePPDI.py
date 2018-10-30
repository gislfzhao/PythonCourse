# Three Narcissistic numbers(pluperfect digital invariant)
s = ''
for i in range(100, 1000):
    if pow(i // 100, 3) + pow(i // 10 % 10, 3) + pow(i % 10, 3) == i:
        s += str(i) + ','
print(s[:-1])
