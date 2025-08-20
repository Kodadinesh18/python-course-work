from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass

class creditcardpayment(payment):
    def make_payment(self,amount):
        print(f"paid ${amount} using credit card.")

class paypalpayment(payment):
    def make_payment(self,amount):
        print(f"paind ${amount} using paypal.")

def process_payment(payment,amount):
    payment.make_payment(amount)

process_payment(creditcardpayment(),100)

process_payment(paypalpayment(),200)
        
