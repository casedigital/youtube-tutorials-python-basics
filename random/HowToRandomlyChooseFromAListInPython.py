# How to randomly choose from a list in python?
# https://youtu.be/OrD49y_G54M

import random


def pick_from_list(lst: list) -> object:
    return random.choice(lst)


def pick_from_list_naive(lst: list) -> object:
    index = random.randint(0, len(lst) - 1)
    val = lst[index]
    return val


if __name__ == "__main__":
    cur_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("-" * 80)
    print("Original: ", cur_lst)
    print("-" * 80, "\n")

    print("-" * 80)
    print("Random Item (Naive): ", pick_from_list_naive(cur_lst))
    print("-" * 80, "\n")

    print("-" * 80)
    print("Random Item (Pythonic): ", pick_from_list(cur_lst))
    print("-" * 80, "\n")
