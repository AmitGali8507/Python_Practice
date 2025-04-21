# Inheritance
from abc import ABC
from abc import abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_info(self):
        pass

class Manager(Employee):
    def get_info(self):
        return f"Manager {self.name} {self.salary}"

class Programmer(Employee):
    def get_info(self):
        return f"Programmer {self.name} {self.salary}"


employees = [
    Manager("Vera", 2000),
    Programmer("Chuck",  1800),
    Programmer("John", 2500)
]

for e in employees:
    print(e.get_info())

