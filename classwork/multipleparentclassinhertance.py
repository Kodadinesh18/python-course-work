class Instagram:
    def __init__(self, username):
        self.username = username
        print(f"{self.username} user is defined parent-1")

class Instav1:
    def __init__(self, username):
        self.username = username
        print(f"{self.username} user is created! parent-2")

class Instav2(Instagram, Instav1):
    def __init__(self, username):
        Instagram.__init__(self, username)
        Instav1.__init__(self, username)
        print("Creating users from version 3")

i = Instav2("Username-Mr_Dinnnu")
