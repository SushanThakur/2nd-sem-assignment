list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged = list1 + list2
result = [x for x in merged if x not in list1 or x not in list2]
print(result)

