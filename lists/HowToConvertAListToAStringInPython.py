# How to convert a list to a string in python?
# https://youtu.be/24ZIhX30NPo

def lst_to_str_with_loops(lst):
    output = ''
    for item in lst:
        output += str(item)
        # output += ' ' + str(item)
    return repr(output)

def lst_to_str_with_join(lst):
    return repr(','.join(lst))

def lst_to_str_with_lst_comprehension(lst):
    return repr(''.join([str(item) for item in lst]))

def lst_to_str_with_map(lst):
    return repr(' '.join(map(str, lst)))


if __name__ == '__main__':
    lst_1 = ['My', 'Name', 'is', 'Jim']
    lst_2 = ['My', 'Name', 'is', 'Jim', 'Im', 20, [1, 2, 3]]

    print('Using Loops: ')
    print('    ', lst_to_str_with_loops(lst_1))
    print('    ', lst_to_str_with_loops(lst_2))

    print('\nUsing Join: ')
    print('    ', lst_to_str_with_join(lst_1))
    # print('    ', lst_to_str_with_join(lst_2))

    print('\nUsing List Comprehension: ')
    print('    ', lst_to_str_with_lst_comprehension(lst_1))
    print('    ', lst_to_str_with_lst_comprehension(lst_2))

    print('\nUsing Map: ')
    print('    ', lst_to_str_with_map(lst_1))
    print('    ', lst_to_str_with_map(lst_2))
