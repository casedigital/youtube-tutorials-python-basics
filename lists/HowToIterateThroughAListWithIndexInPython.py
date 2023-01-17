# How to iterate through a list with index in python?

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 33, 0, 27, 9, 8]
    print("Original: ", my_list)

    for i in range(len(my_list)):
        print(f'Index: {i}   value = {my_list[i]}')

    print('-' * 80)

    for idx, val in enumerate(sorted(my_list)):
        print(f'Method 2: Index: {idx}   value = {val}')
