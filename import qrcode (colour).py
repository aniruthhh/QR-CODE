import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.make("https://www.wikipedia.org/")
img = qr.make_image(fill_color="yellow", back_color="red")
img.save("qrcoloursssc.png")
