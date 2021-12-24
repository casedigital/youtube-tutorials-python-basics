# How To Find the Length Of List In Python?
# https://youtu.be/xozcbxA9AaM

def method_1(lst):
    # For loop
    count = 0
    for item in lst:
        count += 1

    print('Method 1 length = ', count)

def method_2(lst):
    # len method
    print('Method 2 length = ', len(lst))


if __name__ == '__main__':
    cur_list = [1, 2, 3, 4]

    method_1(cur_list)
    method_2(cur_list)
