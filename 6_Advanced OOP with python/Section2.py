class Employee:
    def __init__(self, first_name, middle_name, last_name, salary):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary


    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def raise_salary(self, percentage):
        self.salary = self.salary * (100 + percentage) / 100

    def bonus(self, amount):
        self.salary = self.salary + amount


e1 = Employee("Vera", "Car", "Game", 1000)
e1.raise_salary(12)
e1.bonus(1000)

print(e1.get_full_name())
print(e1.salary)
