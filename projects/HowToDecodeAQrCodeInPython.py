# How to decode a qr code in python
import qrcode
import cv2

if __name__ == "__main__":
    file_name = "MyQRCode.png"
    saying = "This is awesome!"

    img = qrcode.make(saying)
    img.save(file_name)

    detector = cv2.QRCodeDetector()
    qr_text, _, _ = detector.detectAndDecode(cv2.imread(file_name))
    print(f'{qr_text = }')
    if qr_text == saying:
        print('  These are the same!')