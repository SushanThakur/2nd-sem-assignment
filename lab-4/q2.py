import os
from datetime import datetime

CUSTOMER_FILE = "customers.txt"
TRANSACTION_FILE = "transactions.txt"


def load_customers():
    customers = {}
    try:
        with open(CUSTOMER_FILE, "r") as f:
            for line in f:
                name, acc, bal = line.strip().split(",")
                customers[acc] = {"name": name, "balance": float(bal)}
    except FileNotFoundError:
        pass
    return customers


def save_customers(customers):
    with open(CUSTOMER_FILE, "w") as f:
        for acc, data in customers.items():
            f.write(f"{data['name']},{acc},{data['balance']}\n")


def log_transaction(acc, action, amount):
    with open(TRANSACTION_FILE, "a") as f:
        f.write(f"{datetime.now()}, {acc}, {action}, {amount}\n")


def deposit(customers, acc, amount):
    if acc in customers:
        customers[acc]["balance"] += amount
        log_transaction(acc, "Deposit", amount)
        print("Deposit successful.")
    else:
        print("Account not found.")


def withdraw(customers, acc, amount):
    if acc in customers:
        if customers[acc]["balance"] >= amount:
            customers[acc]["balance"] -= amount
            log_transaction(acc, "Withdraw", amount)
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")


def create_account(customers, name, acc, bal):
    if acc in customers:
        print("Account already exists.")
    else:
        customers[acc] = {"name": name, "balance": bal}
        print("Account created successfully.")


customers = load_customers()

while True:
    print("\n--- Banking System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View All Customers")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        n = input("Enter name: ")
        a = input("Enter account number: ")
        b = float(input("Enter initial balance: "))
        create_account(customers, n, a, b)

    elif choice == "2":
        a = input("Enter account number: ")
        amt = float(input("Enter amount: "))
        deposit(customers, a, amt)

    elif choice == "3":
        a = input("Enter account number: ")
        amt = float(input("Enter amount: "))
        withdraw(customers, a, amt)

    elif choice == "4":
        for acc, data in customers.items():
            print(
                f"Name: {data['name']}, Acc: {acc}, Balance: {data['balance']}")

    elif choice == "5":
        save_customers(customers)
        break

    else:
        print("Invalid choice")
