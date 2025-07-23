#1.Automated salary tax caluculator:
salary=float(input())
if salary<=250000:
    print("No Tax")
elif salary>250001 and salary<=500000:
    print(salary*0.05)
elif salary>500000 and salary<=10000000:
    print(salary*0.2)
elif salary >1000000:
    print(salary*0.3)

#2.Movie ticket pricing system:
n=int(input())
total=0
for _ in range(n):
    age=int(input())
    if age>=5 and age<=18:
        total+=100
    elif age>=19 and age<=60:
        total+=150
    elif age>60:
        total+=120
print(total)

#3.#Electrcity Bill Generator
units=int(input())
bill=0
if units<=100:
    bill+=units*1.5
elif units>100 and units<=200:
    bill+=150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
else:
    bill+=1600+(units-500)*6
print(bill)

#4.carparking fee caluculator:
hrs=int(input())
fee=0
if hrs<=2:
    fee=30
    print(fee)
elif hrs>2 and hrs<24:
    fee=30+(hrs-2)*10
    print(fee)
elif hrs>=24:
    fee=200
    print(fee)

#5.product inventory check:
name=input()
quantity=int(input())
if quantity==0:
    print("out of stock")
elif quantity>0 and quantity<=10:
    print("Low stock")
elif quantity>10 and quantity <=50:
    print("In Stock")
elif quantity>50:
    print("overstocked")

#6.pattern:
n=5
for rows in range(n):
    for columns in range(n):
        if (rows+columns)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

#7.Gym subscription billing:
while True:
    print("1.Monthly-500")
    print("2.Quarterly-1300")
    print("3.yearly-5000")
    ch=int(input())
    people=int(input())
    if ch==1:
         print(people*500)
    elif ch==2:
        print(people*1300)
    elif ch==3:
        print(people*5000)
    elif ch==0:
        break
else:
    print("Invalid input")

#8.Billing-bot-apply discount:
total=float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total >4999 and total<1000:
    print(total-total*0.1)
elif total >=10000:
    print(total-total*1.5)

#9.ATM pin verification:

pin=1234
for _ in range(3):

    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked.Try again later.")

#10.bus available seats:
total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f"Total seats:{total_seats}")
print(f"Available-seats:{total_seats-len(booked_seats)}")

        


    


    


    
