print("enter marks out of 100")
a=int(input("enter phy marks"))
b=int(input("enter chem marks"))
c=int(input("enter maths marks"))
d=int(input("enter pcc marks"))
e=int(input("enter eg marks"))
f=int(input("enter python marks"))

total=a+b+c+d+e+f

avg=total/6

print("avg is ",avg)

if avg>=90:
    print("grade is O")
elif avg>=80:
    print("grade is A")
elif avg>=70:
    print("grade is B")
elif avg>=60:
    
    print("grade is C")
    
elif avg>=50:
    print("grade is D")
    
elif avg>=35:
    print("grade is E")
else:
    print("failed")
    
        