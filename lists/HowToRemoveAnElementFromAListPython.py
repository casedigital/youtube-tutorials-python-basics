# how to remove an element from a list python?
# https://youtu.be/hIr-2dEcaGk

from copy import deepcopy

def method_1(lst, el_to_remove):
    # Naive
    new_list = []
    for item in lst:
        if item != el_to_remove:
            new_list.append(item)

    return new_list

def method_2(lst, el_to_remove):
    # remove
    while el_to_remove in lst:
        val = lst.remove(el_to_remove)
        # print(val)
    return lst

def method_3(lst, el_to_remove_idxs):
    # del
    for idx in el_to_remove_idxs:
        # print(len(lst))
        del lst[idx]
        
    return lst

def method_4(lst, el_to_remove_idx):
    # pop
    removed_item = lst.pop(el_to_remove_idx)
    # print('    Now I can use this value of: ', removed_item)
    return lst

def method_5(lst, el_to_remove):
    # remove duplicates
    lst = list(set(lst))
    lst.remove(el_to_remove)
    return lst

if __name__ == '__main__':
    cur_list = [1, 2, 3, 4, 2]

    print(f'Method 1 Removing 2: {method_1(deepcopy(cur_list), 2)}')
    print(f'Method 2 Removing 2: {method_2(deepcopy(cur_list), 2)}')
    print(f'Method 3 Removing 2: {method_3(deepcopy(cur_list), [1, -1])}')
    print(f'Method 4 Removing 2: {method_4(deepcopy(cur_list), 1)}')
    print(f'Method 5 Removing duplicates: {method_5([1, 2, 3, 4, 5, 4, 3, 2, 1], 5)}')
