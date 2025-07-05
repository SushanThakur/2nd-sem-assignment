names = ["Ram", "Shyam", "Ram", "Hari", "Shyam"]
count_dict = {}
for name in names:
    count_dict[name] = count_dict.get(name, 0) + 1
print(count_dict)
