# How to count words in a text file in python?
# https://youtu.be/kE90BE-jd1U

import os


if __name__ == "__main__":
    path_to_txt = os.path.abspath(os.path.join("./", "MyTextFile.txt"))

    text = ""
    with open(path_to_txt, "r") as stream:
        text = stream.read()

    words = text.split()
    print("Words     : ", words)
    print("Word Count: ", len(words))
