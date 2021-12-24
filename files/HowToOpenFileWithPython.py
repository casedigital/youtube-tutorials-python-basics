# How To Open File With Python?
# https://youtu.be/Wq2N7CrkBY8

def method_1():
    file_handler = open('Method1.txt', 'r')
    print(file_handler.readlines())
    file_handler.close()


def method_2():
    with open('Method2.txt', 'r') as file_handler:
        print(file_handler.readlines())


if __name__ == '__main__':

    print('Method 1:')
    method_1()

    print('\nMethod 2:')
    method_2()
