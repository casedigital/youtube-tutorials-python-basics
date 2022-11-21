# how to get all indices of an element in a list in python

import numpy as np

if __name__ == "__main__":
    cur_list = ["Hello", "World", "Hello", "Please", "Subscribe"]
    print(cur_list.index("Hello"))

    indexes = [idx for idx, val in enumerate(cur_list) if val == "Hello"]
    print(indexes)

    indexes_2 = np.where(np.array(cur_list) == "Hello")[0].tolist()
    print(indexes_2)