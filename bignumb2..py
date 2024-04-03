def subtract_bignumbers(num1, num2):
    """
  Subtracts two positive integers represented as strings of digits.

  Args:
      num1: The first number (string).
      num2: The second number (string).

  Returns:
      The difference of the two numbers as a string.
  """
    # Handle cases where one number is shorter than the other
    if len(num1) < len(num2):
        num1 = '0' * (len(num2) - len(num1)) + num1
    elif len(num2) < len(num1):
        num2 = '0' * (len(num1) - len(num2)) + num2

    # Initialize variables for difference and carry
    difference = ""
    carry = 0

    # Iterate through digits from the rightmost position
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        subtraction = digit1 - digit2 - carry

        # Handle negative subtraction results (borrowing from the next digit)
        if subtraction < 0:
            subtraction += 10
            carry = 1
        else:
            carry = 0

        difference = str(subtraction) + difference

    # Remove leading zeros
    difference = difference.lstrip('0')
    if not difference:
        difference = '0'

    return difference


# Read the number of test cases from the first line
with open("general.inp", "r") as f:
    ntest = int(f.readline())

# Process each test case
for _ in range(ntest):
    num1 = f.readline().strip()
    num2 = f.readline().strip()
    result = subtract_bignumbers(num1, num2)
    print(result)