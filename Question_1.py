def sum_multiple(n):
    total = 0

    for i in range(1, n+1):
        if i%3 ==0 or i%5 == 0:
            total += i
    return total

print(sum_multiple(5))


def count_multiple(n):
    count = 0

    for number in range(1,n+1):
        if number%3 == 0 or number%5 == 0:
            count+= 1

    return count
print(sum_multiple(10))

def count_even(n):
    count = 0

    for i in range(1,n+1):

        if i%2 == 0:
            count+= 1

    return count

print(count_even(10))