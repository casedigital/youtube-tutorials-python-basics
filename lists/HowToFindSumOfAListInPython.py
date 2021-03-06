# How To Find Sum Of A List In Python?
# https://youtu.be/ngldO693JYw
from copy import deepcopy

def method_1(lst):
    """ Using Lists """
    lst_sum = 0
    for val in lst:
        lst_sum += val

    print(f'method 1: {lst_sum}')
    return lst_sum

def method_2(lst):
    """ Using sum() function """
    lst_sum = sum(lst)
    print(f'method 2: {lst_sum}')
    return lst_sum

if __name__ == '__main__':
    cur_lst = [1, 2, 3, 4]

    method_1(deepcopy(cur_lst))
    method_2(deepcopy(cur_lst))
