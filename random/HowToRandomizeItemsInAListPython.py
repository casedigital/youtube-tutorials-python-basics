# How to randomize items in a list python?
# https://youtu.be/OGCUSlCQgrc

import random


def randomize_list(lst: list) -> list:
    random.shuffle(lst)
    return lst


if __name__ == "__main__":
    # Create initial List
    cur_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("-" * 80)
    print("Origional: ", cur_list)
    print("-" * 80, "\n")

    # Randomize List
    print("-" * 80)
    print("Randomized: ", randomize_list(cur_list))
    print("-" * 80, "\n")
