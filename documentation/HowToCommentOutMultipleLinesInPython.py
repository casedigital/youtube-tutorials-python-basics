# How to comment out multiple lines in python?

# def add(_a: float, _b: float) -> float:
#     """Add floats

#     Args:
#         _a (float): float value
#         _b (float): float value

#     Returns:
#         float: the sum of _a and _b
#     """
#     val = _a + _b
#     return val

if __name__ == "__main__":
    print("-" * 80)
    # print(add.__doc__)
    print(__doc__)
