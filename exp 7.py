a=int(input("enter a year to check if it is leap year or not"))

if a%4==0 and a%100!=0 or a%400==0:
    print(f"{a} is a leap year")    
else:
    print("not a leap year")
    