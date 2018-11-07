class Customer:
	def __init__(self,name,surname, age):
		self.name = name
		self.surname = surname
		self.age = age
	def __repr__(self):
		return"{}".format(self.name)


class Card:
	def __init__(self,cardType,balance,panNumber,color,association):
		#super().__init__(age)
		self.cardType = cardType
		self.balance = balance
		self.panNumber = panNumber
		self.color = color
		self.association = association
	def __repr__(self):
		return"{}".format(self.cardType)

def type(age,cardType):
	print('\n***Age and card type***')
	if age >= 21 and age <=32:
		cardType = 'Gold'
		print('Card type for this age group is ' + cardType)
	else:
		if age < 32:
			cardType = 'Private Banker'
			print('Card type for this age group is: ' + cardType)
		else:
			cardType = 'Debit'
			print('Card type for age below 21 is ' + cardType)

		

class bankAccount(Card):
	def __init__(self,balance,deposit,withdraw):
		super().__init__(balance)
		self.deposit = deposit
		self.withdraw = withdraw


def getDeposit(balance,deposit):
	print('\n***Deposit amount and print total***')
	result = int(balance) + int(deposit)
	print('Total balance is: ' + str(result))

def getWithdraw(balance,withdraw):
	print('\n***Withdraw amount and print Total***')
	result1 = int(balance) - int(withdraw)
	if(balance < withdraw):
		print("Insuficient funds")
	else:
		if(balance > withdraw):
			print(result1)


def getCards(Cards):
	for n in  Cards:
		print('\nCard details: ' + n.cardType,n.balance, n.panNumber,n.color, n.association)
		

def getCustomers(Customers):
	print('\n ***List of Customers***')
	for l in  Customers:
		print('\nCustomer deatils: ' + l.name,l.surname, l.age)
		
def linkCustomers(Customers,Cards):
	print('\n***Print Link of Customers and Cards')
	for x,y in zip(Customers,Cards):

		print('Customer name: ' + str(x) + " has a " + str(y) + " card")


if __name__ == "__main__":
	
	Customers = []

	
	cus1 = Customer('Sboniso', '\tZondo', 21)
	Customers.append(cus1)
	cus2 = Customer("Sibabalwe", '\tVani', 31)
	Customers.append(cus2)
	cus3 = Customer('Noxolo', '\tPambo', 28)
	Customers.append(cus3)
	cus4 = Customer('Zamathiyane', '\tNcamane', 27)
	Customers.append(cus4)
	cus5 = Customer('Delsy', '\tMabote', 45)
	Customers.append(cus5)
	cus6 = Customer('Thomas', '\tMthiyane', 59)
	Customers.append(cus6)

	Cards = [] 

	c1 = Card('Cheque',100,'\t8799 8665 6455 6544', '\tDebit', '\tVisa')
	Cards.append(c1)
	c2 = Card('Cheque', 23000, '\t6754 4856 0004 9840', '\tGold', '\tVisa')
	Cards.append(c2)
	c3 = Card('Credit', 9000,'\t0000 0000 0000 0000', '\tBlack', '\tMastercard')
	Cards.append(c3)
	c4 = Card('Credit', 25, '\t2634 8763 1728 1240', '\tBlack', '\tMastercard')
	Cards.append(c4)
	c5 = Card('Debit', 5478.25, '\t7676 9067 1236 2763', '\tBlue', '\tAmerican Express')
	Cards.append(c5)
	c6 = Card('Debit', 45625, '\t6325 8132 7863 8730', '\tBlue', '\tAmerican Express')
	Cards.append(c6)
	
	getCards(Cards)
	
	getCustomers(Customers)

	linkCustomers(Customers,Cards)
	#getWithdraw(c3.balance,10000)
	getDeposit(c1.balance,800)
	
	getWithdraw(c3.balance,9100)

	type(cus6.age,c6.cardType)
	type(18,c5.cardType)

