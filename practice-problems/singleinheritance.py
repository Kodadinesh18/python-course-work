class BankAccount:
    
    def __init__(self,balance,accountno):
        self.__balance=balance
        self.__accno=accountno
        
    def deposit(self,amount):
        self.__balance+=amount
        print(f"you added ${amount}, your curent balance is: {self.__balance}")
        
    
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
            print(f"{amount} is successfully debited")
            print(f"your current balance is {self.__balance}")
        else:
            print(f"{amount} is not sufficient in your bank..")
            print(f"your current balance is {self.__balance}")
    
    def get_balance(self):
        print(f"your current balance is: {self.__balance}")
      
    def get_mask(self):
        return "*" * (len(self.__accno) - 4) + self.__accno[-4:]
        

            
acc1=BankAccount(500,"2341234")
print(acc1.get_mask())

acc1.deposit(200)
acc1.withdraw(700)
acc1.get_balance()
            
            
    
    
        

        
    
