# How to read a text file in python?
# https://youtu.be/wabKlJMjo9o

if __name__ == "__main__":
    # Method 1
    cur_file = open("./MyTextFile.txt", "r")
    contents = cur_file.read()
    print(contents)
    cur_file.close()

    print("-" * 80)
    # Method 2
    with open("./MyTextFile.txt", "r") as stream:
        contents = stream.readlines()
        # contents = [val.strip() for val in contents]
        new_contents = []
        for val in contents:
            new_contents.append(val.strip())
        print(new_contents)

    print("Subscribe to Case Digital!")
