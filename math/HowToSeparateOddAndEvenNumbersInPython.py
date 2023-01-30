# how to separate odd and even numbers in python?
import time

if __name__ == "__main__":
    orig_list = list(range(11))
    odds = []
    evens = []

    start = time.time()
    for val in orig_list:
        if val % 2 == 0:
            evens.append(val)
        else:
            odds.append(val)
    end = time.time()
    elapsed_secs = end - start

    # print(f"{orig_list = }")
    # print(f"{evens = }")
    # print(f"{odds = }")
    print(f"{elapsed_secs = :.8f}")
