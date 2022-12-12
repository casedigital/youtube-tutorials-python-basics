# How to swap variables in python?


if __name__ == "__main__":

    var_1 = "Hello"
    var_2 = "World"
    print(f"{var_1 = }")
    print(f"{var_2 = }")

    temp = var_1
    var_1 = var_2
    var_2 = temp
    print('After')
    print(f"{var_1 = }")
    print(f"{var_2 = }")

    var_1, var_2 = var_2, var_1
    print('Ninja')
    print(f"{var_1 = }")
    print(f"{var_2 = }")
