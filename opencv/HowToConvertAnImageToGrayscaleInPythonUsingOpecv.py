# How to convert an image to grayscale in python using opencv?
import cv2
import numpy as np

if __name__ == "__main__":
    img_path = "./test_image.png"
    img = cv2.imread(img_path)
    height, width, channels = img.shape

    print(f"{img.shape = }")

    half_width = width // 2
    left_half = img[:, :half_width, :]
    right_half = img[:, half_width:, :]

    # Convert the right half to grayscale
    right_half_gray = cv2.cvtColor(right_half, cv2.COLOR_BGR2GRAY)

    # Merge the left half (original color) and the right half (grayscale)
    merged_image = np.hstack(
        (left_half, cv2.cvtColor(right_half_gray, cv2.COLOR_GRAY2BGR))
    )
    cv2.imwrite('graysplit.png', merged_image)

    # Display the result
    cv2.imshow('Original and Grayscale Halves', merged_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to create a binary mask of the foreground
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # Convert the mask to 3 channels
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    # Invert the mask to keep the black background
    inv_mask = cv2.bitwise_not(mask)

    # Split the image into color and grayscale parts
    color_part = img[:, :img.shape[1] // 2, :]
    gray_part = cv2.cvtColor(img[:, img.shape[1] // 2:, :], cv2.COLOR_BGR2GRAY)
    gray_part = cv2.cvtColor(gray_part, cv2.COLOR_GRAY2BGR)

    # Resize the grayscale part to match the size of the color part
    gray_part = cv2.resize(gray_part, (color_part.shape[1], color_part.shape[0]))

    # Combine the color part and the inverted mask
    result = cv2.bitwise_and(color_part, inv_mask)

    # Combine the grayscale part and the original mask
    result += cv2.bitwise_and(gray_part, mask)

    # Display the result
    cv2.imshow('Image with Black Background Removed', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()