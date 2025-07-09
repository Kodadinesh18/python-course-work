#1. String Input
name=input("Enter your full name:")
print(name)#Dinesh

#2.Integer Input:
quantity=int(input("enter the number of items:"))
print(quantity)#5

#3.Float Input:
discount=float(input("enter the discount:"))
print(discount)

#input as List(space-separated)
tags=input("enter tags(comma separated:)").split()
#input as List(Coma-separated)
tags=input("enter tags(comma separated:)").split(',')
#input list of integers:
marks=list(map(int,input("enter the list of numbers").split()))
#input set of integers:
marks2=set(map(int,input("enter your marks:").split()))
profile=eval(input())

#Multiple Inputs with Unpacking
username,password=input("enter username and password:").split()
