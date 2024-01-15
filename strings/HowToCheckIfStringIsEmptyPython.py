# How To Check If String Is Empty Python?

if __name__ == "__main__":
    cur_str = " "

    # len_str = len(cur_str.strip())
    # print(f'{len_str = }')
    # if len_str == 0:
    #     print('IS EMPTY')
    # else:
    #     print('IS NOT EMPTY')

    # if cur_str == """""":
    #     print('IS EMPTY')
    # else:
    #     print('IS NOT EMPTY')

    is_empty = not cur_str.strip()
    if is_empty:
        print('IS EMPTY')
    else:
        print('IS NOT EMPTY')

