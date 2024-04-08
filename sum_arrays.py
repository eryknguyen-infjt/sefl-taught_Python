def sum_array(a):
    """
  This function takes an array of numbers and returns the sum of the numbers.

  Args:
      a: A list of numbers.

  Returns:
      The sum of the numbers in the list. If the list is empty, returns 0.
  """

    if not a:
        return 0
    return sum(a)


# Examples
print(sum_array([1, 5.2, 4, 0, -1]))  # Output: 9.2
print(sum_array([]))  # Output: 0
print(sum_array([-2.398]))  # Output: -2.398
