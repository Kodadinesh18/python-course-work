class instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,"-")}")
        
class instagramv1(instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f"bio uploaded")
    
    
    
    
    
Dinesh=instagram('Mr_Dinnnu')

sanjay=instagramv1("kphb-sanjay","coder")

    