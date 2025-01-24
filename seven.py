def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_prime_factors(target):
    i = 2
    prime_factors = []
    while target != 1:
        if target % i ==0:
            prime_factors.append(i)
            target = target // i
        else:
            i = i + 1
            # skipping non-prime numbers
            while i <= target and not is_prime(i):
                i += 1
    return prime_factors


def is_seven_prime(number):
    prime_factors = find_prime_factors(number)

    for factor in prime_factors:
        if factor % 10 != 7:
            return False

    return True


def seven():
    while True:
        number = int(input())
        if number == 0:
            break

        print(f"{number}: {"YES" if is_seven_prime(number) else "NO"}")




seven()
