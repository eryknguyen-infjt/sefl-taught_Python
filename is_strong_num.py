def is_strong(n):
    # Generate a list of prime numbers up to the square root of n
    primes = [2]
    i = 3
    while i ** 2 <= n:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
            if p**2 > i:
                break
        if is_prime:
            primes.append(i)
        i += 2

    # Check if n is divisible by the square of any prime factor
    for p in primes:
        if n % p == 0 and n % (p * p) != 0:
            return False

    return True


strong_numbers = []
for n in range(1, 1001):
    if is_strong(n):
        strong_numbers.append(n)

print(strong_numbers)
