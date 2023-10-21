# How to print on the same line in python

if __name__ == "__main__":
    cur_str = "Programming is awesome! Let's get coding"
    print(cur_str)
    for idx, char in enumerate(cur_str):
        if idx != len(cur_str) -1:
            print(char, end="")
        else:
            print(char)