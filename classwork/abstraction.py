from abc import ABC, abstractmethod

class upload(ABC):
    @abstractmethod
    def compress(self):
        pass
    
class Image(upload):
    def compress(self):
        print("Image is compressed to 2 mb")
        
class Reel(upload):
    def compress(self):
        print("Reel is compressed to 4 mb")
        

reel=Reel()
image=Image()

reel.compress()
image.compress()
