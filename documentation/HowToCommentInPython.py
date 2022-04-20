# How to comment in python?


def add(a, b):
    """
    This adds two numbers

    Args:
        a (int): number
        b (int): number
    """

    c = a + b
    print(f"{c = }")


if __name__ == "__main__":
    # This adds two variables together
    """
    This is a docstring
    """
    a = 5  # This is a magic number (inline comment)
    b = 6
    add(a, b)
    print(add.__doc__)

    add(a, b)

    # This is a block comment (basically the same as single line)
    # a = 5  # This is a magic number (inline comment)
    # b = 6
    # add(a, b)
    # print(add.__doc__)

    # add(a, b)
