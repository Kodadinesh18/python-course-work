#square stars:
for i in range(5):
    for j in range(5):
        print('*',end=" ")
    print()

#output:
'''
         0 1 2 3 4
       0 * * * * * 
       1 * * * * * 
       2 * * * * * 
       3 * * * * * 
       4 * * * * *
'''

for i in range(5):
    for j in range(5):
        print(i,end="")
    print()

#output:
'''
00000
11111
22222
33333
44444
'''

for i in range(5):
    for j in range(5):
        print(j,end="")
    print()
#output:
'''
01234
01234
01234
01234
01234
'''

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#output:
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

'''output:
* * * * * 
* * * * 
* * * 
* * 
* 
'''

for rows in range(5):
    for columns in range(5-rows-1):
        print(" ",end="")
    for columns1 in range(rows+1):
        print("*",end="")
    print()
'''output:
    *
   **
  ***
 ****
*****
'''


for rows in range(5):
    for colums in range(rows):
        print(" ",end="")
    for colums1 in range(5-rows):
        print("*",end="")
    print()

'''output:
*****
 ****
  ***
   **
    *
'''
for row in range(5):
    for column in range(n):
        if row==0 or column==0 or row==n-1 or column==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
output:
*****
*   *
*   *
*   *
*****
'''

for row in range(5):
    for column in range(n):
        if row==0 or column==0 or row==n-1 or column==n-1 or row==n//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

'''output:
*****
*   *
*****
*   *
*****
'''
n=int(input("Enter the number:"))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for rows in range(n):
    for columns in range(n):
        if rows+columns==n-1 or rows==columns:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
        



        








    

