data={
    123456:{"pin":1234,"cb":5000,"history":[]},
    234567:{"pin":1234,"cb":4000,"history":[]},
    345678:{"pin":1234,"cb":7000,"history":[]},
    456789:{"pin":1234,"cb":9000,"history":[]},
    }

accno=int(input("enter your account number: "))
pin=int(input("enter your pin: "))

if accno in data and data[accno]["pin"]:
    print("login successful")
while True:
            print("ATM MENU")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. view Transaction")
            print("5. Exit")
            choice=int(input("enter your choice (1-5)"))
            if choice==1:
                print(f"current Balance:{data[accno]['cb']}")
            elif choice==2:
                d_amount=int(input("enter the amount"))
                data[accno]["cb"]+=d_amount
                data[accno]["history"].append(f"Deposited {d_amount}")
                print(f"Successfully deposited {d_amount}")
            elif choice==3:
                amount=int(input("enter the amount to withdraw:"))
                if data[accno]["cb"]>=amount:
                   data[accno]["cb"]-=amount
                   data[accno]["history"].append(f"Withdrawn amount:{amount}")
                   print(f"Successfully Withdrawn {amount}")
                else:
                    print("INsufficient balance")
            elif choice==4:
                print("Transaction History")
                for i in data[accno]["history"]:
                    print(f"-{i}")
            elif choice==5:
                break
            else:
                print("Invalid option")
                
else:
    print("invalid login")



