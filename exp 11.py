
name = input("Enter Name: ")
basic = float(input("Enter Basic Salary: "))


hra = basic * 0.40
da  = basic * 0.20
ta  = basic * 0.10


pf  = basic * 0.12
tax = basic * 0.10


gross = basic + hra + da + ta
cut= pf + tax
net = gross - cut



print("       SALARY SLIP")

print(f"Name       : {name}")
print(f"Basic      : {basic}")

print(f"HRA (40%)  : {hra}")
print(f"DA  (20%)  : {da}")
print(f"TA  (10%)  : {ta}")

print(f"Gross Salary : {gross}")
print(f"PF   (12%) : -{pf}")
print(f"Tax  (10%) : -{tax}")

print(f"Net Salary   : {net}")
