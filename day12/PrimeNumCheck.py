def is_prime(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False

print(is_prime(75))

