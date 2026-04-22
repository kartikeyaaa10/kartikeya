list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
l=[]

for item in list1:
    if item not in list2 and item not in l:
        l.append(item)
        
print("Unique elements:", l)
