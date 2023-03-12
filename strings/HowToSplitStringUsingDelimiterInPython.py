# how to split string using delimiter in python?

if __name__ == "__main__":
    test = "The  time is now: 1 AM"
    test2 = "act,listen,learn,code"

    print(test.split("now:"))
    print(test2.split(","))
    print(test2.split())
    print(test.split(' '))

    val1, val2, val3, val4 = test2.split(",")
    print(val1)
    print(val2)
    print(val3)
    print(val4)