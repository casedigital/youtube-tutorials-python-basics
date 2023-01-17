# How to change directory in python
import os

if __name__ == "__main__":
    print("-" * 80)
    print("Start: ", os.getcwd())

    # = to "cd FOLDER_PATH" command in terminal
    os.chdir("/Users/zach/Developer")
    print("chdir 1: ", os.getcwd())

    # = to "cd .." command in terminal
    os.chdir("../")
    print("chdir 2: ", os.getcwd())

    os.system("cd /Users/zach/Developer/YouTubeTutorials/youtube-tutorials-python-basics/os_system && touch hello.txt")
    print("os.system: ", os.getcwd())

    print("-" * 80)

