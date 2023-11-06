# How to capture image from webcam using opencv python?
import cv2

if __name__ == "__main__":

    vidcap = cv2.VideoCapture(0)

    while True:
        sucess, frame = vidcap.read()

        if sucess:
            cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vidcap.release()
    cv2.destroyAllWindows()