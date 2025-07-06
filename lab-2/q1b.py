lst = [int(x) for x in input("Enter numbers separated by space: ").split()]

# Find max and min
max_num = lst[0]
min_num = lst[0]
for num in lst:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Maximum:", max_num)
print("Minimum:", min_num)

# Sort list
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)

# Remove duplicates
unique_lst = []
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)
print("List without duplicates:", unique_lst)

