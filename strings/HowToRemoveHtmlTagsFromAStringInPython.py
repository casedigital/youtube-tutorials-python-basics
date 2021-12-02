# How To Remove Html Tags From A String In Python?
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html_str = '<h1><div align=""center"">Apatosaurus (Brontosaurus)</div></h1>'

    text = BeautifulSoup(html_str, features='html.parser').text
    print(text)
