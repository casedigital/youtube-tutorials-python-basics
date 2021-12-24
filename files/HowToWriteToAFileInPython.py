# How To Write To A File In Python?
# https://youtu.be/me0JP3DEZNU

def method_1(text):
    file_handler = open('Method1.txt', 'w')
    file_handler.write(text)
    file_handler.close()


def method_2(text):
    with open('Method2.txt', 'w') as file_handler:
        file_handler.write(text)


if __name__ == '__main__':

    text_to_write = "\n\nSubscribe To Case Digital!\n"
    method_1(text_to_write)
    method_2(text_to_write)
