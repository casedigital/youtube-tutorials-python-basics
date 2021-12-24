# How To Write A Function In Python?
# https://youtu.be/pXsoSvoJmy8


def print_hello():
    print('Hello World')
    print('Hello')
    print('goodbye')


def add(a, b):
    print(f'Proived a = {a} and b = {b}')
    c = a + b
    print(f'Added = {c}')
    return c


if __name__ == '__main__':
    var_1 = add(4, 9)
    var_2 = add(9, 54334)

    print(var_1)
    print(var_2)
