class instagram:
    def __init__(self,username):
        self.username=username
        self.post=[]
        print(f"{self.username.center(40,"-")}")
    def uploadpost(self,image):
        self.image=image
        print(f"{self.image} is uploaded")
        
class instagramv1(instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f"bio uploaded")
    
    def uploadpost(self,image,music):
        def __init__(self,post,music):
            super().uploadpost(post)
            self.music=music
            print(f"{self.music} is added")
        
    
    
    
    
    
Dinesh=instagram('Mr_Dinnnu')
Dinesh.username

sanjay=instagramv1("kphb-sanjay","coder")

    