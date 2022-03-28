# How To Make A Password Generator In Python

import random
import string
import secrets


def method_1(num_chars: int):
    """
    Hand Implemented Method to generate a random password
    of num_chars long

    Args:
        num_chars (int): Number of Characters the password will be

    Returns:
        string: The generated password
    """
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "

    characters = lower + upper + digits + punctuation
    chars_lst = list(characters)

    # Mix up the list
    random.shuffle(chars_lst)

    # Pick random character from list
    password = []
    for i in range(num_chars):
        password.append(random.choice(chars_lst))

    # Shuffle the list for good messure
    random.shuffle(password)

    # Convert list to a string
    password = "".join(password)

    return password


def method_2(num_chars: int):
    """
    Packages implementeation to generate a random password

    Args:
        num_chars (int): Number of Characters the password will be

    Returns:
        string: The generated password
    """
    password = []
    chars = string.ascii_letters + string.digits + string.punctuation

    for i in range(num_chars):
        password.append(random.choice(chars))

    password = "".join(password)

    return password


def method_3(num_chars: int):
    """
    Pythonicish way of generating random password

    Args:
        num_chars (int): Number of Characters the password will be

    Returns:
        string: The generated password
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join((secrets.choice(chars) for i in range(num_chars)))
    return password


if __name__ == "__main__":
    print("\n\n")
    number_of_chars = 50
    password = method_1(number_of_chars)
    print(f"Method 1: New Password = {password} and has length of {len(password)}")

    password = method_2(number_of_chars)
    print(f"Method 2: New Password = {password} and has length of {len(password)}")

    password = method_3(number_of_chars)
    print(f"Method 3: New Password = {password} and has length of {len(password)}")
    print("\n\n")
