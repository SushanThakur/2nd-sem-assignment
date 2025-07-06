tup = (1, 2, 3, 4, 5, 2)
avg = sum(tup) / len(tup)
print("Average:", avg)

# Median
lst = list(tup)
lst.sort()
n = len(lst)
if n % 2 == 0:
    median = (lst[n//2 - 1] + lst[n//2]) / 2
else:
    median = lst[n//2]
print("Median:", median)

# Mode
freq = {}
for num in lst:
    freq[num] = freq.get(num, 0) + 1
mode = max(freq, key=freq.get)
print("Mode:", mode)

