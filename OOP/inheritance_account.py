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
        print("Balance after Deposit is :", self.balance)

    def commit(self):
        with open(self.fp,'w') as file:
            file.write(str(self.balance))
            print("Final Balance is : ",self.balance)


class Checking:

    def __init__(self, filepath): #Contructor for the Checking class
        print("From Checking Class: ")
        Account.__init__(self,filepath) #Calling Account Class construntor



class Savings(Account): # Savings class is Inherting Account class
    """This is a doc string explaining class"""
    classvar = "This is a Class Variable"
    def __init__(self,filepath, fee): #Contructor for the Savings class, passing filepath, and transfer fee
        print("From Savings Class: ")
        Account.__init__(self,filepath)
        self.fee = fee #Assigning value in fee to instance variable self.fee

    def transfer(self,amount):
       self.balance = self.balance - amount - self.fee

chk=Checking("balance.txt")

srid_sav = Savings("Srid_balance.txt",1) # Sending file path and fee while creating object instance
srid_sav.deposit(10000) #Calling deposit function though not defined in Savings Class but is inherited Account class
srid_sav.transfer(1000) #Calling transfer function from Savings which is not defined in parent class Account
srid_sav.commit() # Calling commit function not defined in Saving class but is inherited fromAccount
print(srid_sav.classvar) # classvar sia class variable anc can be accessed by all objcets of a Class


mandy_sav= Savings("Mandy_balance.txt",1)
mandy_sav.deposit(2000)
mandy_sav.transfer(500)
mandy_sav.commit()
print(mandy_sav.classvar) # Anotehr object isnatcne is accessing calss variable classvar

print(mandy_sav.__doc__) # Printing doc string of the class"
