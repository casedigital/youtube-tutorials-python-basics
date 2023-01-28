# How to take arugments from the command line in python?
import os
import sys

if __name__ == "__main__":
    # args = os.sys.argv
    args = sys.argv
    print(f"{args = }")
    script_name = args[0]  # script name
    arg1 = args[1]  # Arg 1
    arg2 = args[2]  # Arg 2
    print(f"{script_name = }")
    print(f"{arg1 = }")
    print(f"{arg2 = }")

    name = arg1
    age = arg2
    print(f"Hello {name} you are {age} years old")
