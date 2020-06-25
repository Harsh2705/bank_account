print("******* WELCOME TO PUNJAB NATIONAL BANK **********")

class bankaccount:
	def __init__(self):
		self.balance=0

	def user(self):
		print("Details of user")
		self.username='Harsh Rana'
		self.account_number='30000841234567'
		self.aadhar_number='784808847077'
		self.phone_number='9027097675'
		self.category='General'
		print('Name:',self.username)
		print('Account number:',self.account_number)
		print('Aadhar number:',self.aadhar_number)
		print('Phone number:',self.phone_number)
		print('Category:',self.category)

	def deposit(self,amount):
		self.balance=self.balance+amount
		print("The amount was deposit in your account is:",self.balance)


	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance-=amount
			print("withdraw amount is:",amount)
		
		else:
			print("you have not money")

	def print_balance(self):
		print("Total balance is:",self.balance)
		return self.balance



account=bankaccount()
account.user()
account.deposit(2000)
account.withdraw(500)
print(account.print_balance())












