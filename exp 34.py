
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


dict1.update(dict2)
print("Merged using update():", dict1)

merged = {**dict1, **dict2}
print("Merged using unpacking:", merged)

