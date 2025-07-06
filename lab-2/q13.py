text = "Hello, World!"
freq = {}
for char in text:
    if char.isalpha():
        freq[char.lower()] = freq.get(char.lower(), 0) + 1
print(freq)

