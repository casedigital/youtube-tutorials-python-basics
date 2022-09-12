# What Is A Class In Python?

class Employee:

    def __init__(self, name:str, title: str, wage_hr: float) -> None:
        self.name = name
        self.title = title
        self.wage_hr = wage_hr

    def calc_income(self, hours_worked: float) -> float:
        return self.wage_hr * hours_worked

def main():
    employee = {
        "name": "John Smith",
        "title": "dev",
        "wage": 60
    }

    employee["wage"] * 60

    cur_employee =  Employee("John Smith", "dev", 60)

    print(employee)
    print(cur_employee.name)
    print(cur_employee.calc_income(40))

if __name__ == "__main__":
    main()
