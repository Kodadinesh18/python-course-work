

data={
      1:{'name':'Dinesh','exam_status':True,'python':100,'sql':95,'html':98},
      2:{'name':'Shivani','exam_status':True,'python':90,'sql':85,'html':88},
      3:{'name':'Arun','exam_status':False,'python':0,'sql':None,'html':None},
      4:{'name':'Darsitha','exam_status':True,'python':40,'sql':35,'html':55},
      5:{'name':'sanjay','exam_status':True,'python':100,'sql':95,'html':98},
    }

for i in data.keys():
    print(f"{i}.{data[i]["name"]}")

studid=int(input("enter the student id:"))

if studid in data:
    
    if data[studid]["exam_status"]==True:
        total=data[studid]["python"]+data[studid]["sql"]+data[studid]["html"]/3
        if(total<90):
            print(f"congrats!,{data[studid]['name']},you got 'A' grade...")
        elif(total<75):
            print(f"good!,{data[studid]['name']},you got 'B' grade...")
        elif(total<35):
            print(f"keep going!,{data[studid]['name']},you got 'c' grade...")
        elif(total<20):
            print("you just passed! the exam")
        else:
            print("you failed in exam!!")
    else:
        print(f"{data[studid]['name']},didnt attempted the exam ")
else:
    print("student id is not existed")

    
    





 
