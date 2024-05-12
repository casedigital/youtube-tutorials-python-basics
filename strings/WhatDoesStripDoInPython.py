# What does strip do in python


if __name__ == "__main__":
    str1 = "Hello, World"
    str2 = " Hello, World\n"
    str3 = "Hello, World          \n\t \r  \n         "
    str4 = "\n\t    Hello, World          \n\t \r  \n         "

    print(f"{str1.strip('LlHhdDeERr') = }")
    print(f'{str2.strip() = }')
    print(f'{str3.strip() = }')
    print(f'{str4.strip() = }')
