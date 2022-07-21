# How to count characters in python?

from collections import Counter


if __name__ == "__main__":
    longest_english_word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
    sentence = "Test this now! Holy cow we are counting characters. What is the most?"

    # Method 1: Count
    print(longest_english_word.count("a"))
    print(sentence.count("a"))
    print("-" * 80)

    # Method 2
    char_dict = {}
    for char in sentence:
        if char not in char_dict:
            char_dict[char] = 0

        char_dict[char] += 1

    sorted_char_list = sorted(char_dict.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_char_list)
    print("-" * 80)

    # Method 3
    method_3 = sorted(Counter(sentence).most_common(), key=lambda x: (-x[1], x[0]))
    print(method_3)
