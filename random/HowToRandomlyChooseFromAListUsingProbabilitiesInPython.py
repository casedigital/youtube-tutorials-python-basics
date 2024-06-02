# How to randomly choose from a list using probabilities in python?

import random

if __name__ == "__main__":
    cur_lst = ["a", "b", "c", "d"]
    one_probs = [.25, .1, .6, 0.05]
    not_one_probs = [4, 3, 6, 1]

    choice = random.choices(cur_lst, k=1, weights=not_one_probs)
    print(f"{choice = }")





