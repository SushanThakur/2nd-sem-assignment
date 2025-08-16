records = [
    {'name': "rice", 'price': 120, 'category': "grocery"},
    {'name': "sugar", 'price': 220, 'category': "grocery"},
    {'name': "wheat", 'price': 320, 'category': "grocery"},
    {'name': "rcereal", 'price': 420, 'category': "grocery"},
]

with open("grocery.txt", "w") as f:
    f.write("ID\tNAME\tPRICE\tCATEGORY\n")
    for i, item in enumerate(records, 1):
        f.write(f"{i}\t{item['name']}\t{item['price']}\t{item['category']}\n")

new_records = []

with open("grocery.txt", "r") as f:
    lines = f.readlines()[1:]  # skip header
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) == 4:
            name = parts[1]
            price = int(parts[2])
            category = parts[3]
            new_records.append(
                {'name': name, 'price': price, 'category': category})

print("records = [")
for item in new_records:
    print(
        f"{{'name':\"{item['name']}\",\"price\":{item['price']},\"category\":\"{item['category']}\"}},")
print("]")
