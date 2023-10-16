# How to display an image in python?
import cv2

if __name__ == "__main__":
    img_path = "./bookCover.png"

    img = cv2.imread(img_path)
    print(img)

    cv2.imshow(img_path, img)
    cv2.waitKey(0)