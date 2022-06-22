# How to make a random color generator in python?
# https://youtu.be/HMOK1aIq4ls

import random
from PIL import Image


def generate_rgb_color() -> tuple:
    # r, g, b -> 0 - 255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


if __name__ == "__main__":

    color = generate_rgb_color()
    print("color: ", color)

    img = Image.new("RGB", (200, 200), color)
    img.show()
