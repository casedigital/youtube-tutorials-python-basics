# How To Sort A List Python?
# https://youtu.be/-ih4OyuVk7k
import random

if __name__ == '__main__':

    # Create Initial List 0-99
    lst = list(range(100))

    # Mix order of the list
    random.shuffle(lst)
    print("Shuffled")
    print(lst)

    # Sort list in place
    print("\nOrdered")
    lst.sort()
    print(lst)

    # Sort list in reverse order in place
    print("\nOrdered Reversed")
    lst.sort(reverse=True)
    print(lst)
