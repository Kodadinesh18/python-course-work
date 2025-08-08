class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        self.avg=sum(self.marks)/len(self.marks)
        if self.avg<35:
            print(f"{self.name}report \n average is {self.avg}\n exam_status:Fali")
        else:
             print(f"{self.name}report \n average is {self.avg}\n exam_status:Pass")

dinesh=student("Dinesh",[10,11,35,90,67])
dinesh.result()
