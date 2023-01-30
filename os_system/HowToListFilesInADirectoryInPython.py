# how to list files in a directory in python
from genericpath import isdir
import os

if __name__ == "__main__":

    dir_to_list = (
        "/Users/zach/Developer/YouTubeTutorials/youtube-tutorials-python-basics"
    )
    print(dir_to_list)

    dir_info = sorted(os.listdir(dir_to_list))
    for file_or_dir in dir_info:
        file_or_dir_path = os.path.join(dir_to_list, file_or_dir)

        if os.path.isdir(file_or_dir_path):
            print(file_or_dir, " Is a directory")

        if os.path.isfile(file_or_dir_path):
            print(file_or_dir, " Is a file")
