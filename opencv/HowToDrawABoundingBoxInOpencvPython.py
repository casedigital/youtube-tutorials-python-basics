# How To Draw A Bounding Box In Python With Opencv?
import cv2

if __name__ == "__main__":
    img_path = "./thumbnail.png"
    img = cv2.imread(img_path)
    x = 868
    y = 18
    w = 269
    h = 385

    cv2.imshow("Before", img)
    cv2.waitKey(0)

    img_with_box = cv2.rectangle(img, (x, y), (x + w, y +h), (0, 0, 255), 15)
    cv2.imshow("With The Box", img_with_box)
    cv2.waitKey(0)

    cv2.destroyAllWindows()