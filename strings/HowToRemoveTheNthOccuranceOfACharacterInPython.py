# How to remove the nth occurance of a character in python?


def remove_nth_occurance(
    input_str: str, char_to_remove: str, occur_to_remove: str
):
    updated_str = ''
    count = 1
    for cur_char in input_str:
        if cur_char != char_to_remove:
            updated_str += cur_char
        else:
            if count != occur_to_remove:
                updated_str += cur_char
            count += 1

    return updated_str


if __name__ == "__main__":
    orig_str = "Charactera"
    print(f"{orig_str = }")

    char_to_replace = 'a'
    occur_to_remove = 2

    new_str = orig_str.replace(char_to_replace, '')
    print(f"{new_str = }")

    new_str2 = orig_str.replace(char_to_replace, '', 1)
    print(f"{new_str2 = }")

    new_str3 = orig_str.replace(char_to_replace, '', 2)
    print(f"{new_str3 = }")

    new_str4 = orig_str[::-1].replace(char_to_replace, '', 1)[::-1]
    print(f"{new_str4 = }")

    new_str5 = remove_nth_occurance(orig_str, char_to_replace, occur_to_remove)
    print(f"{new_str5 = }")