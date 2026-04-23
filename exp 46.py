class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"{self.name}'s new salary after {percentage}% raise: {self.salary}")
        
name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
percentage = float(input("Enter raise percentage: "))

emp = Employee(name, salary)
emp.give_raise(percentage)