import random

main_list = []

for i in range(1, 16):
    main_list.append(random.randint(1, 100))

list_1 = main_list[0:5]
list_2 = main_list[5:10]
list_3 = main_list[10:15]

list_1_sum = sum(list_1)
list_2_sum = sum(list_2)
list_3_sum = sum(list_3)

print("Main list =", main_list)
print("List 1 =", list_1, "Sum =", list_1_sum)
print("List 2 =", list_2, "Sum =", list_2_sum)
print("List 3 =", list_3, "Sum =", list_3_sum)

highest = max(list_1_sum, list_2_sum, list_3_sum)

print("Highest =", highest)

if (highest == list_1_sum):
    print("List 1 has the highest sum")
elif (highest == list_2_sum):
    print("List 2 has the highest sum")
else:
    print("List 3 has the highest sum")
