# how to count unique words from a text file in python?

import os
import string

if __name__ == "__main__":
    path_to_txt = os.path.abspath(os.path.join("./", "MyTextFile.txt"))

    text = ""
    with open(path_to_txt, "r") as stream:
        text = stream.read()

    print("-" * 80)
    # Data Clean up
    text = text.lower()
    for val in string.punctuation:
        if val not in ("'"):
            text = text.replace(val, "")

    # Count Words in a file
    words = text.split()
    print("Words     : ", words, "\n")
    print("Word Count: ", len(words))
    print("-" * 80)

    # Count Unique Words in a file
    words = sorted(set(words))
    print("Unique Words     : ", words, "\n")
    print("Unique Word Count: ", len(words))
    print("-" * 80)
