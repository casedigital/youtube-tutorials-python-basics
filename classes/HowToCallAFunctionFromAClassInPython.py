# how to call a function from a class in python?


class Employee:
    def __init__(self, name: str, title: str, wage_hr: float) -> None:
        self.name = name
        self.title = title
        self.wage_hr = wage_hr

    def calc_income(self, hours_worked: float) -> float:
        return self.wage_hr * hours_worked


if __name__ == "__main__":
    print("Calling a Fuction from a Class in Python!")

    cur_employee = Employee("John Smith", "dev", 50)
    print(cur_employee.calc_income(40))