#Create Account class with 2 attributes- Balance and Account No.
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount ,"was debited")
        print("Total balance is ", self.get_balance())
    
    
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount , "was credited")
        print("Total balance is ", self.get_balance())


    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 124279)
acc1.debit(200)
acc1.credit(2000)
acc1.credit(178000)