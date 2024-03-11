import fractions


def simplify_fraction(fraction_str):
    try:
        # Split the fraction into numerator and denominator
        numerator, denominator = map(int, fraction_str.split('/'))

        # Check if the fraction is valid (denominator != 0)
        if denominator == 0:
            return "Invalid fraction: denominator cannot be 0."

        # Simplify the fraction using the fractions module
        simplified_fraction = fractions.Fraction(numerator, denominator)

        # Return the simplified fraction as a string
        return f"{simplified_fraction.numerator}/{simplified_fraction.denominator}"

    except ValueError:
        return "Invalid input: please enter a fraction in the form 'Numerator/Denominator'."


# Input the fraction from the user
fraction_str = input("Enter a fraction in the form 'Numerator/Denominator': ")

# Simplify the fraction and output the result
simplified_fraction = simplify_fraction(fraction_str)
print(simplified_fraction)