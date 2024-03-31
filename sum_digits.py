def sum_of_digits(n):
    # Calculates the sum of digits in a natural number N.
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10  # Integer division to get the next digit
    return sum


# Write like this is easier than above
'''def sum_of_digits(n):
  Calculates the sum of digits in a natural number N (using recursion).
  if n == 0:
    return 0
  else:
    return n % 10 + sum_of_digits(n // 10)'''

# Read input from a file (replace with input() for interactive use)
with open("general.inp", "r") as file:
    n = int(file.readline())

# Calculate the sum of digits
sum_digits = sum_of_digits(n)

# Write output to a file (replace with print() for interactive use)
with open("general.out", "w") as file:
    file.write(str(sum_digits))

print("Sum of digits written to general.out")  # Confirmation message

