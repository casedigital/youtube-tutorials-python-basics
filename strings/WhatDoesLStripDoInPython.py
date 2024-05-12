# What does lstrip do in python


if __name__ == "__main__":
    str1 = "Hello, World"
    str2 = "     \n\t \r  \n           Hello, World"
    str3 = "Hello, World          \n\t \r  \n         "

    print(f"{str1.lstrip('Hello, ') = }")
    print(f"{str2.lstrip('Hello, ') = }")
    print(f"{str3.lstrip() = }")