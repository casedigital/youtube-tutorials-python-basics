# How To Get Input From User In Python
# https://youtu.be/UacrMdJX8kA

if __name__ == '__main__':

    user_input = ''
    while user_input != 0:
        user_input = int(input("Enter your age: "))

        print(f'User entered {user_input} with type {type(user_input)}')
