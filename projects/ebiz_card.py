# How to create a business card with python?
import qrcode
import vobject

if __name__ == "__main__":
    
    vcard = vobject.vCard()
    vcard.add("version")
    vcard.version.value = "3.0"
    # vcard.add("version").value = "3.0"

    # Name
    vcard.add("fn")
    vcard.fn.value = "John Smith"

    # Phone
    vcard.add("tel")
    vcard.tel.value = "+1555-555-5555"
    vcard.tel.type_param = "WORK"

    # Email
    vcard.add("email")
    vcard.email.value = "test@example.com"
    vcard.email.type_param = "INTERNET"

    serailized_vcard = vcard.serialize()

    print(serailized_vcard)

    qr = qrcode.QRCode()
    qr.add_data(serailized_vcard)
    qr.make(fit=True)

    img = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 0, 0))
    img.save("./MyBizCard.png")
