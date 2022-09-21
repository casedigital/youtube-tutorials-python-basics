# how to create an instance of a class in python?

class Employee:

    def __init__(self, name:str, title: str, wage_hr: float) -> None:
        self.name = name
        self.title = title
        self.wage_hr = wage_hr

    def calc_income(self, hours_worked: float) -> float:
        return self.wage_hr * hours_worked

employee_1 = Employee("John Smith", "Dev", 100000)
employee_2 = Employee("Jane Smith", "Boss", 150000)

print(f'{employee_1.name = }')
print(f'{employee_1.title = }')
print(f'{employee_1.wage_hr = }')
print(f'{employee_2.name = }')
print(f'{employee_2.title = }')
print(f'{employee_2.wage_hr = }')