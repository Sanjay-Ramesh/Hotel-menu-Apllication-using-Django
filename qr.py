import qrcode

image = qrcode.make("https://127.0.0.1:8001")
image.save("qr.png")