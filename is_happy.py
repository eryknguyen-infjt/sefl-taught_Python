def is_happy(n):
    # Set of numbers that we have visited before
    visited = set()

    while n != 0 and n not in visited:
        # Add the number to the set of visited numbers
        visited.add(n)

        # Calculate the sum of the squares of the digits
        n = sum(int(digit) ** 2 for digit in str(n))

    return n == 1


birthday = 44
if is_happy(birthday):
    print(f"{birthday} is a happy number!")
else:
    print(f"{birthday} is not a happy number.")
