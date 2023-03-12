# what is an instance variable in python?

class Person:
    id = 123
    def __init__(self, name,) -> None:
        self.name = name
        self.age = 30

if __name__ == "__main__":
    cur_person = Person("Jim")
    print(f"{cur_person.name = }")

    cur_person2 = Person("Jane")
    print(f"{cur_person2.name = }")

    print('-'*80)
    cur_person.name = 'Jimmy'
    print(f"{cur_person.name = }")
    print(f"{cur_person2.name = }")

    print('-'*80)
    print(dir(cur_person))
    print('~'*80)
    print(dir(Person))