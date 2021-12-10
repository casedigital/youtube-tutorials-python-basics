# How To Remove Spaces From A String In Python?
# https://youtu.be/DHxYe8sS048
import re

if __name__ == '__main__':
    space_str = 'You will  benefit from subscribing    to Case Digital'
    print(f'\nOriginal: {space_str}')

    # Replace
    no_spaces_str = space_str.replace(' ', '')
    print(f'Replace : {no_spaces_str}')

    # Split Join
    no_spaces_str = ''.join(space_str.split())
    print(f'Split   : {no_spaces_str}')

    # Regex
    pattern = r'\s+'
    no_spaces_str = re.sub(pattern, '', space_str)
    print(f'Regex   : {no_spaces_str}')

    print('\n')
