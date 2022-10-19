# How to debug a program with arguments in vscode?

import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument(
        "-s", "--saying", help="Description for foo argument", required=True
    )
    parser.add_argument(
        "-f", "--foo", help="Description for foo argument", required=True
    )
    args = vars(parser.parse_args())
    return args


def test_function(my_str):
    my_str += " Subscribe to Case Digital!"
    return my_str


if __name__ == "__main__":
    # saying = os.sys.argv[1]
    # print(test_function(saying))
    
    args = parse_args()
    print(test_function(args['saying']))
