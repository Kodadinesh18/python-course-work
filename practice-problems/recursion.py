def sumofnum(n):
    if n==1:
        return 1
    return n+sumofnum(n-1)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

n=int(input("enter the number: "))
print(sumofnum(n))
print(fact(n))
                
