import qrcode as qr
a=input("enter the link to make QR code:")
code=qr.make(a)
code.show('hi.png')
