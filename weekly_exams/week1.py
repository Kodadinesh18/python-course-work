#Q.1: the birthday format fixer(String & type conversion):
date,month,year=input().split("-")
print(f"{year}/{month}/{date}")
#input:15-07-2025
#output:2025/07/15

#2.the even odd game:
number=int(input())
if number%2==0:
    print("Even Winner")
else:
    print("Odd number")
#input:70
#output:Even Winner 

#3.vowel replacer bot(String methods):
String=input().lower()
print(String.translate(str.maketrans("aeiou","*****")))
#input:my name is dinesh
#output:my n*m* *s d*n*sh

#4.Shopping cart Analyzer(List operations):
prices=list(map(float,input().split(",")))
print(f"maxprices:{max(prices)}")
print(f"total price:{sum(prices)}")
#input:10, 20, 30, 10.8,4.7
#output:
#maxprices:30.0
#total price:75.5

#5.Secure login system(tuple & conditions):

credentials=("admin","python123")
username=input()
password=input()
if username==credentials[0] and password==credentials[1]:
    print("Login Succesful")
else:
    print("Access Denied")
#output:
    #input:dinsh
    #input:dinesh@123
    #output:Access Denied

#6.Remove Duplicates from set(set operations):
names=set(input().split(','))
names=list(names)
print(names)
#inputs:dinesh,sanjay,prsanth,krupal,krupal,revanth,jaswath,revanth,sanjay
#outputs: ['krupal', 'prsanth', 'jaswath', 'revanth', 'sanjay', 'dinesh']

#7.Student Marks Record(Dictionary method):
max_marks = 0
res = ""
students = int(input("Enter number of students: "))
students_list = {}

for i in range(students):
    name, marks = input("Enter name and marks (comma-separated): ").split(",")
    marks = int(marks)
    students_list[name] = marks
    if marks > max_marks:
        max_marks = marks
        res = name
print(res)
"Enter number of students: 4
"Enter name and marks (comma-separated): Dinesh,97
"Enter name and marks (comma-separated): Sanjay,87
"Enter name and marks (comma-separated): krupal,98
"Enter name and marks (comma-separated): prasanth,99
"prasanth

#8.reversing my string:
sentence=input().split()
for i in sentence:
    print(i[::-1],end=" ")
#input:hello world
#output:olleh dlrow

#9.clean my list:
numbers=list(map(int,input().split()))
new_list=[]
for i in range(len(numbers)):
    if numbers[i]!=0:
        new_list.append(numbers[i])
print(new_list)

#input:0 1 11 33 0 2
#output:[1, 11, 33, 2]

#10.the frequency counter:

statement = input("Enter a string: ").replace(" ", "")  # Removes all white spaces
frequency = {}

for char in statement:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

print(frequency)







        
    







    
