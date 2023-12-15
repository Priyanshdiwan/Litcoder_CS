def min_set_size(num, k):
    num = int(num)
    if k.isspace():
        k = 0
    else:
        k = int(k)
    if num == 0:
        return 0
    for i in range(1, 10):
        if (k * i) % 10 == num % 10 and (k * i) <= num:
            return i
    return -1
num = input()
k = input()
print(min_set_size(num, k))