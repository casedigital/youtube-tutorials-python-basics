# how to delete files in python
import os

if __name__ == "__main__":
    root_file_to_be_removed_path = './DELETE_ME'

    for filename in os.listdir(root_file_to_be_removed_path):
        if filename.endswith('.txt'):
            complete_filepath = os.path.join(root_file_to_be_removed_path, filename)
            print(complete_filepath)
            os.remove(complete_filepath)