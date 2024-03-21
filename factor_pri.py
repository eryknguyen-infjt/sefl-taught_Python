from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_pairs(k):
    prime_pairs = []
    for a in range(2, k):
        if is_prime(a):
            b = k - a
            if is_prime(b):
                prime_pairs.append((a, b))
    return prime_pairs


a = b = 0


def sumPrimes_ofK(test_cases):
    results = []
    for k in test_cases:
        prime_pairs = find_prime_pairs(k)
        if prime_pairs:
            results.append(f"{k} = {prime_pairs[0][0]} + {prime_pairs[0][1]}")
        else:
            results.append(f"{k} = NO SOLUTION")
    return results


def read_input(fname):
    with open(fname, 'r') as file:
        n = int(file.readline())
        test_cases = [int(line) for line in file.readlines()]
    return n, test_cases


def write_output(fname, results):
    with open(fname, 'w') as findout:
        for result in results:
            findout.write(result + '\n')


def main():
    n, test_cases = read_input('general.inp')
    results = sumPrimes_ofK(test_cases)
    write_output('general.out', results)

# if in different file we write: from factor_pri.py import * ,or only write: import factor_pri.py


if __name__ == "__main__":
    main()
