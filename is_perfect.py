def is_perfect_number(n):
    sum_of_divisors = 0
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
            divisors.append(i)

    if sum_of_divisors == n:
        return True, divisors
    else:
        return False, []


def main():
    n = int(input("Enter a 2-digit natural number: "))
    if 10 <= n <= 99:
        perfect, divisors = is_perfect_number(n)
        if perfect and divisors:   # or only perfect
            print(f"{n} is a perfect number.")
            print("Divisors:", divisors)
        else:
            print(f"{n} is not a perfect number.")
    else:
        print("Please enter a 2-digit natural number.")


if __name__ == "__main__":
    main()











