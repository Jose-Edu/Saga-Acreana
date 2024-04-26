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

    image.save(f'\\output\\{output_name}.png', 'png')


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

    image.save(f'\\output\\{output_name}.png', 'png')


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

    image.save(f'\\output\\{output_name}.png', 'png')


if __name__ == '__main__':

    teams_data = read_temp(2023)
    teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')
    comps = dict()

    comps_text = dict()
    comps_text['Acreano'] = (('É CAMPEÃO', 'ACREANO!'), 'Campeonato Acreano')
    comps_text['Copa Verde'] = (('É CAMPEÃO', 'DA COPA VERDE!'), 'Copa Verde')
    comps_text['Brasileirão'] = (('É CAMPEÃO', 'DA SÉRIE'), 'Brasileirão')
    comps_text['Copa do Brasil'] = (('É CAMPEÃO', 'DA COPA DO BRASIL!'), 'Copa do Brasil')
    comps_text['Sula.'] = (('É CAMPEÃO', 'DA SUL-AMERICANA!'), 'Copa Sul-Americana')
    comps_text['Liberta.'] = (('É CAMPEÃO', 'DA LIBERTADORES!'), 'Copa Libertadores')
    comps_text['Super Copa'] = (('É CAMPEÃO DA', 'SUPERCOPA DO BRASIL!') , 'SuperCopa do Brasil')
    comps_text['Recopa Sula.'] = (('É CAMPEÃO DA', 'RECOPA SUL-AMERICANA!'), 'Recopa Sul-Americana')

    for comp in teams_data['Acre'].keys():
        comps[comp] = list()
        for team in teams_data.keys():
            comps[comp].append(teams_data[team][comp])

    for comp in comps:
        winner = False
        for team in range(0, len(comps[comp])):
            if comps[comp][team] in ('Campeão') or '1º' in comps[comp][team]:
                winner = True
                if comp == 'Brasileirão':
                    serie = f' {comps[comp][team][-2]}!'
                    img_club_info((teams[team], 'confete', 'taça', 'acesso'), (comps_text[0][comp][0], comps_text[0][comp][1]+serie[-2]), f'{teams[team]} campeão {comp}')
                else:
                    img_club_info((teams[team], 'confete', 'taça', 'acesso'), comps_text[0][comp], f'{teams[team]} campeão {comp}')
        if not winner:
            img_6clubs_info(comps[comp], comps_text[comp][1].upper(), f'resultados {comp}')