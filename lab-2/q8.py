all_students = {1, 2, 3, 4, 5}
cricket = {1, 2, 3}
football = {2, 3, 4}

print("Both sports:", cricket & football)
print("Only one sport:", (cricket ^ football))
print("Neither:", all_students - (cricket | football))

