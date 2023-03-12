# What is a class attribute python?

class Employee:
    company_zip = 1234
    company_state = "Idaho"

    def __init__(self, name) -> None:
        self.name = name

if __name__ == "__main__":
    e1 = Employee("Jim")
    e2 = Employee("Jane")
    e3 = Employee("Kate")

    print(f"{e1.name = }")
    print(f"{e2.name = }")
    print(f"{e3.name = }")

    print(f"{e1.company_zip = }")
    print(f"{e2.company_zip = }")
    print(f"{e3.company_zip = }")
    print(f"{e1.company_state = }")
    print(f"{e2.company_state = }")
    print(f"{e3.company_state = }")

