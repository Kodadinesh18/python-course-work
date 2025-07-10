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
#output:wait for 3 more years! to vote

#nested-conditions:
#Example: Amazon Stock with Prime Customer Priority
amazon_stock=3
prime_member=True

if amazon_stock > 0:
    print("product is avaialble")
    if prime_member:
        print("you have free shipping!")
    else:
        print("Standard shipping will apply.")
else:
    print("the product is out of stock")

'''output:
product is avaialble
you have free shipping!
'''

#practice questions:
#1.
amazon_stock=5
if amazon_stock>0:
    print("the product is available")
    if amazon_stock<=5:
        print("the product is limited")
else:
    print("the product is out of stock!")
'''output:
the product is available
the product is limited'''

#2.
discount_coupon=True
if discount_coupon:
    print("you can avail your free prime access!")
else:
    print("sorry! there is no discount coupon for this account")
#output:you can avail your free prime access!

#3.positive-neagative-zero??
n=int(input("enter the number: "))
if n>0:
    print("it is a positive number!")
elif n<0:
    print("it is a negative number!")
elif n==0:
    print("it is zero!")


