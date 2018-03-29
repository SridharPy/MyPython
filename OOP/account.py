class Account:

    def __init__(self,filepath):
        self.fp= filepath
        with open(filepath , 'r') as file:
            self.balance=int(file.read())
            print(self.balance)

    def withdraw(self,amt):
        if amt <= self.balance:
            self.balance= self.balance - amt
        else:
            print("Insufficient balance")

    def deposit(self,amt):
        self.balance = self.balance + amt
        print(self.balance)

    def commit(self):
        with open(self.fp,'w') as file:
            file.write(str(self.balance))
            print(self.balance)


acc = Account("balance.txt")
acc.deposit(100)
acc.withdraw(150)
acc.commit()
