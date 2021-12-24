# How To Find Index of Item In List Python?
# https://youtu.be/GuKSxX0D1oc?


def method_1(lst, item_to_find):
    # With loop
    found_idx = None
    for idx, item in enumerate(lst):
        if item == item_to_find:
            found_idx = idx
            break

    print('method 1a: at index', found_idx)

    count = 0
    for item in lst:
        if item == item_to_find:
            found_idx = count
            break
        count += 1

    print('method 1b: at index', found_idx)

def method_2(lst, item_to_find):
    # With index function
    print('method_2: at index', lst.index(item_to_find))


if __name__ == '__main__':
    
    cur_lst = [1, 2, 3, 4]
    # method_1(cur_lst, 3)
    method_2(cur_lst, 3)

