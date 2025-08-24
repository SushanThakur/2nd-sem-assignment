class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}. New Balance = ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New Balance = ₹{self.__balance}")
        else:
            print("Insufficient Balance!")

    def get_details(self):
        print(f"Account Number: {self.__account_number}, Balance: ₹{self.__balance}")


# Example
acc1 = BankAccount(123456789, 5000)
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(6000)
acc1.get_details()
