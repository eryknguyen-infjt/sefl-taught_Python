import math
from math import *


def find_p(a):
    # Compute the product of all elements in the sequence
    p = 1
    for x in a:
        p *= x

    # Find the smallest perfect square number that is greater than or equal to p
    sq = math.isqrt(p) + 1
    while (sq * sq) % 2 == 0:
        sq += 1
    while (sq * sq) % 3 == 0:
        sq += 1
    while True:
        if (sq * sq) % 5 == 0:
            sq += 1
        else:
            break
    p = sq * sq

    # Multiply p by the smallest prime factors of each element in the sequence
    # to ensure that p is divisible by all elements
    for x in a:
        if x == 1:
            continue
        p *= find_smallest_prime_factor(x)

    return p % 10 ** 7


def find_smallest_prime_factor(n):
    # Find the smallest prime factor of n using trial division
    if n % 2 == 0:
        return 2
    for p in range(3, int(math.sqrt(n)) + 1, 2):
        if n % p == 0:
            return p
    return n


n = int(input())
a = list(map(int, input().split()))

print(find_p(a))

# def find_p(n, a):
# p = 1
# for x in a:
# p *= x

# i = 2
# while i * i <= p:
# if p % i:
# i += 1
# else:
# p //= i

# return p

# n = int(input())
# a = list(map(int, input().split()))

# print(find_p(n, a))
