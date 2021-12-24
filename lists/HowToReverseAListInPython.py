# How To Reverse a list in python?
# https://youtu.be/bkVeJc39AI4

from copy import deepcopy


def method_1(lst):
    # With loop
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])

    print('method 1: ', reversed_lst)


def method_2(lst):
    # With Slicing
    print('method_2: ', lst[::-1])


def method_3(lst):
    # With list in place method
    print('method_3: ', lst)
    lst.reverse()
    print('method_3: ', lst)


def method_4(lst):
    # With reversed function
    print('method_4: ', reversed(lst))
    print('method_4: ', list(reversed(lst)))


if __name__ == '__main__':

    cur_lst = [1, 2, 3, 4]
    # method_1(deepcopy(cur_lst))
    # method_2(deepcopy(cur_lst))
    # method_3(deepcopy(cur_lst))
    method_4(deepcopy(cur_lst))
