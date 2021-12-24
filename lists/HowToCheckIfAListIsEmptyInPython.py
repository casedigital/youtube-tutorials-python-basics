# How To Check If A List Is Empty In Python?
# https://youtu.be/VS9km2_ALIM

def method_1(lst):
    is_empty = len(lst) == 0
    print('  Method 1 is empty: ', is_empty)

    if len(lst) == 0:
        print('    Empty')

def method_2(lst):
    # using bool
    is_empty = not lst
    print('  Method 2 is empty: ', is_empty)

    if lst:
        print("     Not empty")


if __name__ == '__main__':
    cur_list = [1, 2, 3, 4]
    empty_list = []

    print('Using a non empty list: ', cur_list)
    method_1(cur_list)
    method_2(cur_list)

    print('Using an empty list: ', empty_list)
    method_1(empty_list)
    method_2(empty_list)
