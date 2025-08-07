#example on encapusulation


'''class Details:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password
    def viewpwd(self):
        return self.__password
    def changepassword(self,newpassword):
        self.__password=newpassword

dinesh=Details("Dinesh","kodadinesh18@gmail.com","Dinesh@123")

print(dinesh.name)
print(dinesh._email)
dinesh._email="kosafwe@gmail.com"
print(dinesh._email)
print(dinesh.viewpwd())
dinesh.changepassword("Deepak")
print(dinesh.viewpwd())'''


#explanation of encapsulation:
'''without underscore- public 
with single underscore - private
with double underscore - protected
'''


class Bank:
    def __init__(self):
        self._balance=0
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,amount):
        self._balance+=amount


Dinesh=Bank()
print(Dinesh.balance)
Dinesh.balance=1000
print(Dinesh.balance)




