class shopping:
    discount=10

    def product(self,name,price):
        self.name=name
        self.price=price



user1=shopping()
user2=shopping()

user1.name="laptop"
user1.price=4999


print(user1.name)
print(user1.price)
print(shopping.discount)
