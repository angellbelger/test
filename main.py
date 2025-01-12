import qrcode

datas = {'01': "https://segmuc.altamira.pa.gov.br/"}

if __name__ == '__main__':
    for i, (key, value) in enumerate(datas.items()):
        qr = qrcode.QRCode(None, qrcode.ERROR_CORRECT_H)
        qr.add_data(value)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(f'img/{key}.png')