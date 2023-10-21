# How To Select A Bounding Box In Python With Opencv?
import cv2

if __name__ == "__main__":
    img_path = "./thumbnail.png"
    img = cv2.imread(img_path)
    print(img)

    x, y, w, h = cv2.selectROI("Select ROI", img, fromCenter=False, showCrosshair=False)

    print(
        f"{x = }   {y = }   {w = }   {h = }"
    )
