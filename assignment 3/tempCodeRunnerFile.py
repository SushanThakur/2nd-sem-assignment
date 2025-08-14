records = [
    {'name': "rice", 'price': 120, 'category': "grocery"},
    {'name': "sugar", 'price': 220, 'category': "grocery"},
    {'name': "wheat", 'price': 320, 'category': "grocery"},
    {'name': "cereal", 'price': 420, 'category': "grocery"},
]

# Writing to grocery.txt
with open("grocery.txt", "w") as f:
    f.write("ID\tNAME\tPRICE\tCATEGORY\n")
    for idx, record in enumerate(records, start=1):
        line = f"{idx}\t{record['name']}\t{record['price']}\t{record['category']}\n"
        f.write(line)

# Reading from grocery.txt
print("Reading records from file:\n")
with open("grocery.txt", "r") as f:
    content = f.read()
    print(content)
