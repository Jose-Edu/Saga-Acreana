import psd_tools as psd_
from PIL import ImageDraw, ImageFont

def img_club_info(layers=(), texts=('', ''), output_name='image'):

    psd = psd_.PSDImage.open('info_time.psd')

    for l in layers:
        layer_var = list(filter(lambda layer: layer.name == l, psd.descendants()))[0]
        layer_var.visible = True

    image = psd.composite(force=True)

    img = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=72)
    img.text((300, 120), texts[0], font=font, fill='white', anchor='mm')

    img = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=64)
    img.text((300, 480), texts[1], font=font, fill='white', anchor='mm')

    image.save(f'{output_name}.png', 'png')