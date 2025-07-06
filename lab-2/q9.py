import random
nums = set()
while len(nums) < 10:
    nums.add(random.randint(1, 100))

nums = list(nums)
print("Original set:", nums)
nums.remove(max(nums))
nums.remove(min(nums))
print("After removing min & max:", nums)

