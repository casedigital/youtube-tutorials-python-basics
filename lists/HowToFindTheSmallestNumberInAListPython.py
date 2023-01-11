# How to find the smallest number in a list python


if __name__ == "__main__":
    cur_list = [1, 2, 4, 9, 5, 10, 33, 0]
    print(cur_list)

    # Method 1: loops
    smallest = cur_list[0]
    for num in cur_list:
        if num < smallest:
            smallest = num
    print("Method 1: ", smallest)

    # Method 2: sorting
    smallest2 = sorted(cur_list)[0]
    print("Method 2: ", smallest2)

    # Method 3: Min
    smallest3 = min(cur_list)
    print("Method 3: ", smallest3)
