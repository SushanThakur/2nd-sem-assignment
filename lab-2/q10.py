sentence = input("Enter sentence: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
found = set()

for char in sentence:
    if char in vowels:
        found.add(char)

print("Unique vowels:", found)

