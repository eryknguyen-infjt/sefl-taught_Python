def find_substring(string1, string2):
    """
  This function checks if string2 is in string1 and returns the first position and number of occurrences.

  Args:
      string1: The first string to search.
      string2: The second string to search for.

  Returns:
      A tuple containing the first position (or -1 if not found) and the number of occurrences of string2 in string1.
  """
    first_pos = -1
    count = 0
    n = len(string2)
    for i in range(len(string1) - n + 1):
        if string1[i:i + n] == string2:
            if first_pos == -1:
                first_pos = i
            count += 1
    return first_pos, count


# Get string inputs from the user
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

# Find the substring and print the results
first_position, num_occurrences = find_substring(string1, string2)

if first_position == -1:
    print(f"String '{string2}' is not found in string '{string1}'.")
else:
    print(f"String '{string2}' found in string '{string1}' at position {first_position + 1} ({num_occurrences} times).")
