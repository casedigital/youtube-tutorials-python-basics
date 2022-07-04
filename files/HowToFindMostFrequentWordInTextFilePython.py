# how to find most frequent word in text file python?
# https://youtu.be/jMuZXiDeuPo

from collections import Counter
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

    print(text)
    freq_dict = {}
    for word in words:
        freq_dict[word] = text.count(word)

    print("-" * 80)
    print(freq_dict)
    print("-" * 80)
    common_occurance_lst = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    print(common_occurance_lst)

    print("-" * 80)

    word_occurance = Counter(text.split()).most_common()
    print(word_occurance)
    for word in word_occurance:
        print(word[0], word[1])
