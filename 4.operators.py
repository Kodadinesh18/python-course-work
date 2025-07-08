#operators in python

#1.Arithmetic operators

a=30
b=20

#addition(+)
print("Addition of a and b is:",a+b) #50

#subtraction(-)
print("Subtraction of a and b is:",a-b) #10

#multiplication(*)
print("Multiplication of a and b is:",a*b) #600

#Division(/)
print("Division of a and b is:",a/b) #1.5

#floor division(//)
print("Floor Division of a and b is:",a//b)#1

#modulo(%)
print("Modulo of a and b is:",a%b)#10

#exponential(**)
print("Square of a is:",a**2)#900

#========================================================================================

#2.Comparision operators(it returns a boolean output)

c=10
d=40

#Equal to
print("Equal (==):",c==d) #False

#Not equal
print("Not Equal (!=):",c!=d) #True

#Greater than
print("greater than (>):",c>d) #False

#Less than
print("less than (>):",c<d) #True

#Greater than or Equal to
print("greater than or equal to (>=):",c>=d) #False

#Less than or equal to
print("Less than or equal to (<=):",c<=d) #True

#=========================================================================================

#3.Assignment operators

#Assign
x=30
print("Assign(=)",x) #Assign(=) 30

#Exponential and assign
x**=3
print("Exponential and assign(**=)",x)#Exponential and assign(**=) 27000

#Add & Assign
x+=5
print("Add and Assign(+=)",x)#Add and Assign(+=) 27005

#subtract & Assign
x-=5
print("subtract and Assign(-=)",x)#subtract and Assign(-=) 27000 

#Multiply & Assign 
x*=5
print("Multiply and assign(*=)",x)#Multiply and assign(*=) 135000

#Divide & Assign
x/=5
print("Divide and assign(/=)",x) #Divide and assign(/=) 27000.0

#floor divide & Assign
x//=3
print("floor divide and assign(//=)",x) #floor divide and assign(//=) 9000.0

#Modulus & Assign
x%=11
print("modulus and assign (%=)",x) #modulus and assign (%=) 2.0

#========================================================================================

#4.Logical operators(used to combine multiple conditions):

e=10
f=30

#AND
print(e%10==0 and f%10==0)

#OR
print(e%2==0 or f%2==0)

#NOT
print(not e%2==0)

#========================================================================================

#5.Membership operators

zoo=["Monkey","Elephant","cheetah","tiger","Lion"]

#in
print("Monkey" in zoo) #True

#notin
print("dog" not in zoo) #True

print("M" in zoo[0]) #True

#========================================================================================

#6.identity operators

one=[1,2,3]
print("id(one):",id(one))#id(one): 1770245955968
two=one
print("id(two):",id(two))#id(two): 1770245955968
three=[1,2,3]
print("id(three):",id(three))#id(three): 1770290656256
#is
print(one is two)# Output: True (Both refer to the same

print(one is three)# Output: False (Different objects with the
print(one is not three)# Output: True

#=======================================================================================

#7.bitwise operators

x = 5 # Binary: 0101
y = 3 # Binary: 0011
print(x & y) # Output: 1 (Binary: 0001 → AND operation)
print(x | y) # Output: 7 (Binary: 0111 → OR operation)
print(x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print(~x) # Output: -6 (Binary: Inverts bits of 5)
print(x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)

#=========================================================================================


















      


















