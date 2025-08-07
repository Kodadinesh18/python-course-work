class status:
    def uploadImage(self,imageurl):
        self.image=imageurl
        print(f"{self.image} is uploaded to your status")
        
class statusv1(status):
    def addcaption(self,text=None):
        self.caption=text
        print(f'"{self.caption}" is added to your status')

class statusv2(status):
    def like(self):
        print(f'you can like status')

class statusv3(statusv1,statusv2):
    def addMusic(self,music):
        self.music=music
        print(f"{self.music}....is added to your status")

class statusv4(statusv3):
    def videolength(self,video):
        self.video=video
        print(f"{self.video}is uploaded to your status")



sanjay=statusv4()
sanjay.uploadImage("sanjay.png")
sanjay.addcaption("my life")
sanjay.like()
sanjay.videolength('d44r.mp3')