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
        
dinesh=status()
dinesh.uploadImage('selfie.png')

sanjay=statusv1()
sanjay.uploadImage('Goodmorning.png')
sanjay.addcaption("Morning friends!")

krupal=statusv2()
krupal.uploadImage("Cofee.png")
krupal.like()