from math import sqrt


def is_prime(num):
    # Check if the number is less than 2 (the smallest prime number)
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):  # sqrt(num) == num**0.5
        if num % i == 0:
            return False
    return True


def sum_of_primes(a, b):
    prime_sum = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum


# Input two integers A and B (0<a<B)
a = int(input("Enter the first integer (0<a<B): "))
b = int(input("Enter the second integer (0<a<B): "))


def multiples_of_five(a, b):
    print(f"Numbers divisible by 5 from {a} to {b}:")
    for num in range(a, b + 1):
        if num % 5 == 0:
            print(num)


# Validate the input
if a < 0 or a >= b or b <= 0:
    print("Invalid input. Please ensure 0 < a < B.")
else:
    # Find and calculate the sum of prime numbers in the sequence from A to B
    prime_sum = sum_of_primes(a, b)
    print(f"The sum of prime numbers from {a} to {b}: {prime_sum}")

    # Output to the screen the numbers divisible by 5 in the sequence from A to B
    multiples_of_five(a, b)