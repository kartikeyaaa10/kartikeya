a=[]
for i in range (22):
    b=int(input(f"Enter number {i+1}: "))
    a.append(b)
print(a)

a=set(a)
print('after removing duplicates we get',a)