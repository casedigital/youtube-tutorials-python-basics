# How to get terminal output in python?
import os
import subprocess

if __name__ == "__main__":

    cmd = ['ls', 'noexisting.png']
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    print(result)
    print(result.stdout)