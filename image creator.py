import psd_tools as psd_
from PIL import ImageDraw, ImageFont
from read_temp import read_temp

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


def img_6clubs_info(teams_txt = ('A', 'A', 'C', 'F', 'R', 'S'), title = 'TITLE', output_name = 'image'):

    psd = psd_.PSDImage.open('info6teams.psd')
    image = psd.composite()
    img = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=64)

    txt_key = 0
    
    for y in (220, 380):
        for x in (100, 300, 500):
            img.text((x, y), teams_txt[txt_key], font=font, fill='white', anchor='mm')
            txt_key+=1

    img.text((300, 300), title, font=font, fill='white', anchor='mm')

    image.save(f'{output_name}.png', 'png')


def img_tumb(teams=('Acre', 'Silvestre'), comp='Copa', fase='8/F', desc='ida e volta', output_name='image'):

    psd = psd_.PSDImage.open('tumb.psd')

    layer_var = list(filter(lambda layer: layer.name == teams[0]+'_e', psd.descendants()))[0]
    layer_var.visible = True
    layer_var = list(filter(lambda layer: layer.name == teams[1]+'_d', psd.descendants()))[0]
    layer_var.visible = True

    image = psd.composite(force=True)
    img = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='ARIBLK.TTF', size=128)
    img.text((960, 166), f'{teams[0]} x {teams[1]}'.upper(), font=font, fill='white', anchor='mm')
    font = ImageFont.truetype(font='ARIBLK.TTF', size=72)
    img.text((960, 276), comp, font=font, fill='white', anchor='mm')
    img.text((960, 358), fase, font=font, fill='white', anchor='mm')
    font = ImageFont.truetype(font='ARIBLK.TTF', size=64)
    img.text((960, 436), desc, font=font, fill='white', anchor='mm')

    image.save(f'{output_name}.png', 'png')


if __name__ == '__main__':

    teams_data = read_temp(2022)
    comps = dict()

    for comp in teams_data['Acre'].keys():
        comps[comp] = list()
        for team in teams_data.keys():
            comps[comp].append(teams_data[team][comp])