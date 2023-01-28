# How To Do Math In Python?

if __name__ == '__main__':
    a = 5
    b = -5
    c = 2.5
    e = 2

    d = a + c
    print(f'{a} + {c} = {d}')

    d = b - b
    print(f'{b} - {b} = {d}')

    d = b*(1 + 3)
    print(f"{b} * (1 + 3) = {d}")
    print(f'{b} * {b} = {d}')

    d = a // e
    print(f'Division: {a} // {e} = {d}')

    d = e**(2+a*(b+a)/ 5)
    print(f'{e} raised {2+a*(b+a)/ 5} = {d}')

    d = a % e
    print(f'{a} % {e} = {d}')