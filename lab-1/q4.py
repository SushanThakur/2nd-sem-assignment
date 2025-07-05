string = "hello world"
count_dict = {}
for char in string:
    count_dict[char] = count_dict.get(char, 0) + 1
print(count_dict)
