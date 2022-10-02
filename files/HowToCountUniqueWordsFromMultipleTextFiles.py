# how to count unique words from multiple text files in python?
# https://youtu.be/OvCDSULHhoI

from doctest import master
import os
import string


def get_unique_words_from_str(text: str) -> list:

    # Data Clean up
    text = text.lower()
    for val in string.punctuation:
        if val not in ("'"):
            text = text.replace(val, "")

    # Count Words in a file
    words = text.split()

    # Count Unique Words in a file
    words = sorted(set(words))

    return words


def get_unique_words(path_to_file: str) -> list:
    text = ""
    with open(path_to_file, "r") as stream:
        text = stream.read()

    return get_unique_words_from_str(text)

    # # Original Function
    # # print("-" * 80)
    # # Data Clean up
    # text = text.lower()
    # for val in string.punctuation:
    #     if val not in ("'"):
    #         text = text.replace(val, "")

    # # Count Words in a file
    # words = text.split()
    # # print("Words     : ", words, "\n")
    # # print("Word Count: ", len(words))
    # # print("-" * 80)

    # # Count Unique Words in a file
    # words = sorted(set(words))
    # # print("Unique Words     : ", words, "\n")
    # # print("Unique Word Count: ", len(words))
    # # print("-" * 80)

    # return words


if __name__ == "__main__":
    path_to_txt = os.path.abspath(os.path.join("./", "MyTextFile.txt"))
    path_to_txt_1 = os.path.abspath(os.path.join("./", "file_1.txt"))
    path_to_txt_2 = os.path.abspath(os.path.join("./", "file_2.txt"))

    master_unique_words = []
    # # When using files
    # for file_path in [path_to_txt, path_to_txt_1, path_to_txt_2]:
    #     unique_words = get_unique_words(file_path)
    #     print("Unique Words     : ", unique_words, "\n")
    #     print("Unique Word Count: ", len(unique_words))
    #     print("-" * 80)
    #     master_unique_words = master_unique_words + unique_words

    # When using massive string
    file_contents = ""
    for path_to_file in [path_to_txt, path_to_txt_1, path_to_txt_2]:
        with open(path_to_file, "r") as stream:
            file_contents += stream.read() + "\n"

    print(file_contents)
    master_unique_words = get_unique_words_from_str(file_contents)

    print(
        "Master Unique Words     : ",
        master_unique_words,
        len(master_unique_words),
        "\n",
    )
    master_unique_words = list(set(master_unique_words))
    print("Master Unique Words     : ", master_unique_words, "\n")
    print("Master Unique Word Count: ", len(master_unique_words))
    print("-" * 80)
