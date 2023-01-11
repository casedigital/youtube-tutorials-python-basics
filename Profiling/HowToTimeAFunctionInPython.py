# How to time a function in python

import time
import timeit

def add(a, b) -> int:
    return a + b


if __name__ == "__main__":

    start = time.time()
    my_sum = add(5, 55)
    end = time.time()
    elapsed = end - start
    print(f'Elapsed Time : {elapsed:.6f} seconds')

    elapsed2 = timeit.timeit(lambda: add(5, 55), number=1)
    print(f'Elapsed Time2: {elapsed2:.6f} seconds')

