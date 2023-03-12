# How to copy a file in python?
import shutil

if __name__ == '__main__':
    file_to_be_copied_path = './hello.txt'
    copy_dst = '../'
    # copy_dst = '/Users/zach/Developer/YouTubeTutorials/youtube-tutorials-python-basics/hello.txt'

    shutil.copy(file_to_be_copied_path, copy_dst)
