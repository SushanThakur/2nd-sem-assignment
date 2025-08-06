class BankAccount:
	def __init__(self, name, acc_no):
		self.name = name
		self.account = acc_no
		self.balance = 0
		self.history = []
		
	def deposite(self, amt):
		self.balance += amt
		self.history.append({
			'method': 'deposite', 'amount': amt
		})
	
	def withdraw(self, amt):
		if(self.balance < amt):
			print("Insufficient Balance")
			return
		else:
			self.balance -= amt
			self.history.append({
			'method': 'withdraw', 'amount': amt
		})
			
	def checkBalance(self):
		return f'Your current Balance is: Rs. {self.balance}'
	
ob1 = BankAccount("Ram", "1011")
ob1.withdraw(100)
ob1.deposite(10000)
ob1.withdraw(500)
print(ob1.checkBalance())
print(ob1.history)
for record in ob1.history:
	print(record)
