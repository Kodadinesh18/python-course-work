class user:
    def __init__(self,username,password,premium_subscription):
        self.username=username
        self.__password=password
        self.premium_subscription=premium_subscription


user1=user("Dinesh","DInesh@2003",True)
print(user1.username);
