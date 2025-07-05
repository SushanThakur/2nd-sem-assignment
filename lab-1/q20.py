num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Sum:", num1 + num2)
elif choice == 2:
    print("Difference:", num1 - num2)
elif choice == 3:
    print("Product:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Quotient:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
