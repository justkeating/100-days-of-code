import qrcode

data = 'Don\'t forget to subscribe'

img = qrcode.make(data)

img.save('/Users/kenny/Documents/100-days-of-code/paddles/myqrcode.png')