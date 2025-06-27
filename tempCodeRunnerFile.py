import random

main_list = []

for i in range(1,16):
    main_list.append(random.randint(1,100))
    
list_1 = main_list[0:5]
list_2 = main_list[5:10]
list_3 = main_list[10:15]

print(main_list)
print(list_1)
print(list_2)
print(list_3)

list_1_sum = 0
list_2_sum = 0
list_3_sum = 0

for i in list_1:
    list_1_sum += i
for i in list_1:
    list_1_sum += i
for i in list_1:
    list_1_sum += i

print(list_1_sum)