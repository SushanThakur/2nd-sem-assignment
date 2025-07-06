lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Maximum:", max(lst))
print("Minimum:", min(lst))
lst.sort()
print("Sorted list:", lst)
lst = list(set(lst))
print("List without duplicates:", lst)

