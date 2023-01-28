# How To Check If A String Is Palindrome In Python?
import string


def remove_punc_and_spaces(input: str) -> str:
    for punc in string.punctuation + " ":
        input = input.replace(punc, "")

    return input


if __name__ == "__main__":
    palindromes = [
        "12/21/33 12:21",
        "madam",
        "Mr. Owl ate my metal worm",
        "eve",
        "Bob",
        "33",
        "121",
    ]
    non_palindromes = ["owl", "case", "teacher"]

    for cur_str in palindromes + non_palindromes:
        non_punc_str = remove_punc_and_spaces(cur_str).lower()
        reversed_str = non_punc_str[::-1]
        is_palindrome = non_punc_str == reversed_str
        print(f"{non_punc_str} == {reversed_str} is palindrome = {is_palindrome}")
