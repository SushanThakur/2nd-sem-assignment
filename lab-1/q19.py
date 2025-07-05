for num in range(100, 1000):
    if sum(int(digit)**3 for digit in str(num)) == num:
        print(num, end=" ")
