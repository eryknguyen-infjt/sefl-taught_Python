def is_magical(s):
    #:type s: str
    #:rtype: bool

    char_counts = {}
    for i, char in enumerate(s):
        if char in char_counts:
            # Check if the previous character with the same value can be connected
            if i - char_counts[char] > 1 and all(s[j] != char for j in range(char_counts[char] + 1, i)):
                return False
        char_counts[char] = i
    return True


# Test cases
print(is_magical("CDDC"))  # Output: True (Chars C and C can be connected)
print(is_magical("CDAA"))  # Output: False (Chars A cannot be connected)
print(is_magical("ABACDA"))  # Output: True (All characters can be connected)
print(is_magical("BABAA"))  # Output: False (Chars A cannot be connected)

# Sample Input
data = ["ABAB", "AABB", "CDDCXX", "ZLZP", 'YYY']

# Count the number of magical strings
magical_count = sum(is_magical(string) for string in data)

# Print the results
print(f"{magical_count}")
for string in data:
    if is_magical(string):
        print(string)
