import qrcode as qr
img= qr.make("https://www.wikipedia.org/")
img.save("wiki.png")
