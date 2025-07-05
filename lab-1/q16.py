nums = [int(x) for x in input("Enter 10 numbers: ").split()]
pos = sum(1 for x in nums if x > 0)
neg = sum(1 for x in nums if x < 0)
zero = sum(1 for x in nums if x == 0)
print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")
