# https://www.youtube.com/@CaseDigital
# How to call a function in python


def print_hello():
    print("Hello")


def add(a, b):
    c = a + b
    return c


if __name__ == "__main__":
    print_hello()
    v = add(5, 5)
    print(v)