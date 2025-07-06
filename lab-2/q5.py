lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for i in range(len(lst)):
    is_prime = lst[i] > 1 and all(lst[i] % j != 0 for j in range(2, int(lst[i] ** 0.5) + 1))
    if i % 2 == 0 or is_prime:
        result.append(lst[i])

print(result)

