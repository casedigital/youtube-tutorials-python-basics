# How To Iterate Through A String In Python

if __name__ == "__main__":
    cur_string = "Programming is awesome! Let's get coding"
    print(cur_string)

    # Method 1: Loop with Indexes
    for i in range(len(cur_string)):
        print(f'Index: {i} = {cur_string[i]}')

    print('-' * 80)

    # Method 2: Loop without Indexes
    for char in cur_string:
        print(char)