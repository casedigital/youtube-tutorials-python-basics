# How to do selection sort in python?
import random


def selection_sort(arr):
    len_arr = len(arr)

    for i in range(len_arr):
        min_idx = i
        for j in range(i + 1, len_arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # print(f'before: {arr}')
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print(f'  after: {arr}')
    return arr


if __name__ == "__main__":
    cur_list = [random.randint(1, 50) for _ in range(10)]
    print(f'{cur_list = }')
    print('-' * 80)

    ordered_list = selection_sort(cur_list.copy())
    print(f'{ordered_list = }')
    print('-' * 80)
