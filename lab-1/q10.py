d = {}
n = int(input("How many pairs? "))
for _ in range(n):
    key = input("Key: ")
    value = input("Value: ")
    d[key] = value

search_key = input("Search key: ")
print(d.get(search_key, "Key not found"))
