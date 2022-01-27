### Follow: https://pypi.org/project/qrcode/
# and https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/
import qrcode

qr = qrcode.QRCode(version = 1, 
                    box_size = 20, 
                    border = 0)
qr.add_data('https://github.com/chrbeckm/ors-2022-tampa-poster-2146')
qr.make(fit=True)

img = qr.make_image(fill_color = 'black', back_color='#84b819')
img.save('qrcode-poster.png')
