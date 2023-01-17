# how to remove duplicates from a list in python?


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 5, 3, 33, 0, 0]
    print('Original: ', my_list)

    # Method 1: Loops
    non_dup = []
    for val in my_list:
        if val not in non_dup:
            non_dup.append(val)

    print('Method 1: ', non_dup)

    # Method 2: set
    non_dup2 = list(set(my_list))
    print('Method 2: ', non_dup2)

    # Bonus: Maintain list order
    non_dup3 = list(dict.fromkeys(my_list))
    print('Method 3: ', non_dup3)