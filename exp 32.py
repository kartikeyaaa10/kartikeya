
student = {
    "name"  : "Raj",
    "age"   : 20,
    "branch": "FE",
    "cgpa"  : 9.2
}


print("Keys =", list(student.keys()))

print("Values =", list(student.values()))


print("\n Student Details ")
for k, v in student.items():
    print(k, ":", v)