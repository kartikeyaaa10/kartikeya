a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))

s=input("enter the operation you want to perform +,-,*,/")

if s=="+":
    print("the sum is",a+b)
elif s=="-":
    print("the difference is",a-b)
elif s=="*":
    print("the product is",a*b)
elif s=="/":
    print("the quotient is",a/b)
    
else:
    print("invalid sign")