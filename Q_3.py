def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num+1):
        if num % i == 0:
            return False

        return True


def get_prime(limit):
    primes = []
    for i in range(2, limit+1):
        if is_prime(i):
            primes.append(i)

    return primes


print(get_prime(10))