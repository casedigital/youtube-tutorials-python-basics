# What does rstrip do in python


if __name__ == "__main__":
    str1 = "Hello, World"
    str2 = " Hello, World"
    str3 = "Hello, World          \n\t \r  \n         "

    print(f"{str1.rstrip() = }")
    print(f"{str2.rstrip() = }")
    print(f"{str3.rstrip() = }")
    print(repr(str3.rstrip()))