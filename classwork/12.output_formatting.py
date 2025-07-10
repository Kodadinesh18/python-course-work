#basic printing a text:
print("hello.World!")#hello.World!

#printing multiple items:
name="Dinesh"
batch="PFS-30"
print("name: ",name,"batch: ",batch)#name:  Dinesh batch:  PFS-30

#using sep:
print("2025","07","10",sep="-")#2025-07-10

#using end:
print("hello","python",end=" ")#hello python

#new line:
print("line1\nline2")#it prints in new line

#\tab: it provides 4 spaces:
print("hello\t,world")#hello   ,world

#output formatting methods:
name="dinesh"
age=21
cgpa=7.95

#1.comma-separated:
print("name: ",name,"Age: ",age,"cgpa: ",cgpa)
#output:name:  dinesh Age:  21 cgpa:  7.95

#2.using modulo operator:
print("name:%s | Age:%d | cgpa: %f" %(name,age,cgpa))
#output:name:dinesh | Age:21 | cgpa: 7.950000

#3.f-strings:
print(f"name:{name} age:{age} cgpa:{cgpa}")
#output:name:dinesh age:21 cgpa:7.95

#str.format()method:
print("Name: {} Age: {} cgpa: {}".format(name,age,cgpa))

