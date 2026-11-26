def reverse_num(n):
    reverse_num = 0

    while n>0:
        digit = n %10
        reverse_num = reverse_num * 10+ digit
        n = n// 10

    return reverse_num

print(reverse_num(1234))