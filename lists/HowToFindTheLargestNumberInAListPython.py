# How To Find The Largest Number In A List Python

if __name__ == '__main__':
    cur_list = [1, 2, 4, 9, 5, 10, 33, 0]
    print(cur_list)

    # Method 1: loop
    largest = cur_list[0]
    for num in cur_list:
        if num > largest:
            largest = num
    print('Method 1: ', largest)

    # Method 2: Sorting
    sorted_list = sorted(cur_list)
    largest2 = sorted_list[-1]
    print('Method 2: ', largest2)

    # Method 3: Max
    largest3 = max(cur_list)
    print('Method 3: ', largest3)
