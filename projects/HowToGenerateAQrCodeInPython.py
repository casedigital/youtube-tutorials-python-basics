# how to generate a qr code in python
import qrcode

if __name__ == "__main__":
    file_name = "MyQRCode.png"
    saying = "This is awesome!"

    img = qrcode.make(saying)
    img.save(file_name)
