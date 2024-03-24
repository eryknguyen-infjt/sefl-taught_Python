# Function to find the GCD of two numbers using Euclidean algorithm
def gcd(x, y):  # stands for greatest common divisor
    while y:
        x, y = y, x % y
    return x


# Function to find the GCD of three numbers
def gcd_of_three(a, b, c):
    return gcd(gcd(a, b), c)


# Get input from the user
num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))
num3 = int(input("Enter third positive integer: "))

# Check if the inputs are positive integers
if num1 > 0 and num2 > 0 and num3 > 0:
    # Calculate the GCD of the three numbers
    result = gcd_of_three(num1, num2, num3)
    print(f"The greatest common divisor of {num1}, {num2}, and {num3} is: {result}")
else:
    print("Please enter positive integers only.")
