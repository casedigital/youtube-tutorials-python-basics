# How to empty your python list
import copy

if __name__ == "__main__":
    a = [1, 2, 3]
    # b = copy.copy(a)
    b = a
    print(f'Before: {a = }')
    print(f'Before: {b = }')
    # a.clear()
    b.clear()
    # b = []
    # a = []
    print(f'After: {a = }')
    print(f'After: {b = }')