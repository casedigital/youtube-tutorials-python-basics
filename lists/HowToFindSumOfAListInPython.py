# How To Find Sum Of A List In Python?
# https://youtu.be/ngldO693JYw

def method_1(lst):
    lst_sum = 0
    for val in lst:
        lst_sum += val

    print(f'method 1: {lst_sum}')

def method_2(lst):
    lst_sum = sum(lst)
    print(f'method 2: {lst_sum}')

if __name__ == '__main__':
    
    cur_lst = [1, 2, 3, 4]
    # method_1(cur_lst)
    method_2(cur_lst)
