'''
In Python, the main types of conditional statements are:
1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested Conditional Statements
'''

#example for if condition:
age=18
if age>=18:
    print("eligible for voting")
#output:eligible for voting

#if-else example:
age=17
if age>=18:
    print("eligible for voting!")
else:
    print("not eligible for voting!")
#output:not eligible for voting!

#if-elif-else-example:
age=15
if(age>=18):
    print("eligible for voting")
elif(age==15):
    print("wait for 3 more years! to vote")
else:
    print("you are not eligible for voting!")
