# how to get all attributes of a python object

class Employee:
    company_zip = 1234
    company_state = "Idaho"

    def __init__(self, name) -> None:
        self.name = name

    def add():
        print('Hello')

if __name__ == "__main__":
    e1 = Employee("Jim")

    print(dir(e1))
    new_atters = [attr for attr in dir(e1) if not callable(getattr(e1, attr)) and not attr.startswith('__')]
    print('-'*80)
    print(new_atters)

    new_atters = []
    for attr in dir(e1):
        if not callable(getattr(e1, attr)) and not attr.startswith('__'):
                new_atters.append(attr)

    print('-'*80)
    print('Round 2: ', new_atters)

