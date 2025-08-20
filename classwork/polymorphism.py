class normaluser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with : \n 1.Normal quality\n 2.Ads run")

class premiumuser(normaluser):
    def playvideo(self,name):
        print(f"\n{name} is playing video with : \n 1.High quality\n 2.no Ads run")
def play_video(user,username):
    user.playvideo(username)

dinesh=normaluser()
sanjay=premiumuser()
mohit=normaluser()
gopal=normaluser()
        
play_video(dinesh,"dinesh")
play_video(sanjay,"sanjay")
play_video(mohit,"mohit")
play_video(gopal,"gopal")