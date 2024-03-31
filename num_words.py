text = input("Enter a piece of Vietnamese text (without accent marks): ")

# Split the text into words
words = text.split()

# Count the total number of characters
total_chars = len(text)

# Count the number of words
num_words = len(words)

# Create a dictionary to store character counts
char_counts = {}
for char in text:
    if char not in char_counts:
        char_counts[char] = 0
    char_counts[char] += 1

# Print the results
print("Total number of characters:", total_chars)
print("Total words:", num_words)

for char, count in char_counts.items():
    print(f"Character '{char}': {count}")

