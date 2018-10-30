# The sum of integers about plus and minus
int_sum = 0
for i in range(1, 967):
    int_sum += i * pow(-1, i - 1)
print(int_sum)
