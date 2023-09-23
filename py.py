import csv
class DictionaryAPIen:
    def __init__(self, csv_han):
        self.api_en = csv_han

# Next steps: we'll use CRUD(create, read, update, delete) -> C = lookup, R = add, U = update, D = delete
    def lookup(self, word, definition): # C
        with open(self.api_en, mode='r') as file:
            reader = csv.DictReader(file)
            for k in reader:
                if k[word] == word:
                    return k[definition]
        return f" '{word}' not found in the dictionary."

    def add(self, word, definition):
        with open(self.api_en, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=['word', 'definition'])
            writer.writerow({'word': word, 'definition': definition})

    def update(self, word, n_definition):
        data = dict()
        with open(self.api_en, mode='r') as file:
            reader = csv.DictReader(file)
            for k in reader:
                if k[word] == word:
                    k['definition'] = n_definition
                data.append(k)

        with open(self.api_en, mode='r') as file:
            writer = csv.DictWriter(file, fieldnames=['word', 'definition'])
            writer.writeheader()
            writer.writerows(data)

    def delete(self, word):
        content = dict()
        with open(self.api_en, mode='r') as file:
            reader = csv.DictReader(file)
            for k in reader:
                if k[word] != word:
                    content.append(k)

        with open(self.api_en, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['word', 'definition'])
            writer.writeheader()
            writer.writerows(content)

if __name__ == '__main__':
    dictionary = DictionaryAPIen('dict.csv')

    while True:
        print("\nDictionary Menu (choice):")
        print("1. Lookup word.")
        print("2. Add word.")
        print("3. Update definition.")
        print("4. Delete word.")
        print("5. Exit.")

        choice = input('Enter your choice: ')

        if choice == '1':
            word = input('Enter any word: ')
            definition = dictionary.lookup(word)
            print(f"{word}: {definition}")

        elif choice == '2':
            word = input('Enter a new word: ')
            definition = input("Enter the definition: ")
            dictionary.add(word,definition)
            print(f"'{word}' has been added to the dictionary.")

        elif choice == '3':
            word = input('Enter any word: ')
            new_definition = input('Enter the new definiton: ')
            dictionary.update(word, new_definition)
            print(f"'{word}' has been updated.")

        elif choice == '4':
            word = input('Enter any word: ')
            dictionary.delete(word)
            print(f"'{word}' has been deleted from the dictionary.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a valid option.")







