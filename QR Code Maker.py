import qrcode as qr
from PIL as x
a=input("enter the link to make QR code:")
code=qr.make(a)
code.show()
