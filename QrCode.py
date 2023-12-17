# install all libraries we needed
# create a function that collect a text and convert it into qr code
# save the qr code as image
# run a functiion
import qrcode


def gerrate_qrcode(text):

    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fil_color="" , back_color="pink")
    img.save("qrimg.png")


gerrate_qrcode(" https://wa.me/+92 -(311)8203633")