# How to replace one character in a string in python?


def replace_nth_char(
    input_str: str, orig_char: str, new_char: str, which_orig_char: int
):
    start = 0
    for i in range(which_orig_char):
        idx = input_str.find(orig_char, start)
        if idx == -1:
            return input_str
        start = idx + 1

    new_str = f"{input_str[:idx]}{new_char}{input_str[idx+1:]}"
    return new_str


if __name__ == "__main__":
    cur_string = "glowwormw"
    new_char = 'm'
    char_to_replace = 'w'
    which_char_count_to_replace = 1

    print('\n')
    print('-' * 80)
    print(f"{cur_string = }")
    updated_str = replace_nth_char(
        cur_string, char_to_replace, new_char, which_char_count_to_replace
    )
    print(f"{updated_str = }")
    print('-' * 80, '\n')
