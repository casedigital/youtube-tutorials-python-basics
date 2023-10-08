# How To Remove One Of N Characters In Python?

if __name__ == "__main__":

    sentence = "This is an example sentence with repeating characters in a word."
    char_to_remove = "a"
    print(f"Orig {sentence = }")

    new_sentence1 = sentence.replace(
        char_to_remove, ''
    )
    print(f"{new_sentence1 = }")

    new_sentence2 = sentence.replace(
        char_to_remove, '', 1
    )
    print(f"{new_sentence2 = }")

    new_sentence3 = sentence.replace(
        char_to_remove, '', 2
    )
    print(f"{new_sentence3 = }")

    new_sentence4 = sentence.replace(
        char_to_remove, '', -2
    )
    print(f"{new_sentence4 = }")

    print(f"Reversed = {sentence[::-1]}")
    new_sentence5 = sentence[::-1].replace(
        char_to_remove, '', 2
    )[::-1]
    print(f"{new_sentence5 = }")

    word_to_fix = "characters"

    words = sentence.split(" ")
    print(words)
    new_sentence6 = []
    for word in words:
        if word == word_to_fix:
            word = word.replace(
                char_to_remove, '', 1
            )
        new_sentence6.append(word)

    new_sentence6 = ' '.join(new_sentence6)
    print(f"{new_sentence6 = }")
