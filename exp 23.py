my_list = [10, 5, 20, 8, 15]
largest = my_list[0]

for num in my_list:
    if num > largest:
        largest = num

print(f"The largest element in the list is {largest}")
