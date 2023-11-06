# How to crop an image in opencv python?
import cv2

if __name__ == "__main__":
    img_path = "./thumbnail.png"
    img = cv2.imread(img_path)
    x = 868
    y = 18
    w = 269
    h = 385

    cv2.imshow("Test", img)
    cv2.waitKey(0)

    top_left = (x, y)
    bottom_right = (x + w, y + h)

    crop_img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    cv2.imshow("ROI", crop_img)
    cv2.waitKey(0)
    