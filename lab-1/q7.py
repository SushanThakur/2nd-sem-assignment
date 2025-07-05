d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
merged = d1.copy()
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)
