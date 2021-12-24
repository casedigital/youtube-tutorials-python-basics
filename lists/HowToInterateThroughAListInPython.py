# How To Iterate Through a List In python?
# https://youtu.be/8YQ2X1NGdEc

def method_1(lst):
    # For loop
    lst_str = ""
    for item in lst:
        print(item)
        lst_str += str(item) + " "

    print('For Loop: ', lst_str)

def method_2(lst):
    # While loop
    lst_str = ""
    count = 0
    while count < len(lst):
        item = lst[count]
        lst_str += str(item) + " "
        count += 1

    print('While Loop: ', lst_str)

def method_3(lst):
    # For loop and range
    lst_str = ""
    for i in range(len(lst)):
        print(i)
        item = lst[i]
        lst_str += str(item) + " "

    print('For Loop and range: ', lst_str)


if __name__ == '__main__':
    cur_list = [1, 2, 3, 4]

    method_1(cur_list)
    method_2(cur_list)
    method_3(cur_list)
