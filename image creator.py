import psd_tools as psd_
from PIL import ImageDraw, ImageFont, Image
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

    image.save(f'output\\{output_name}.png', 'png')
    image.close()


def img_6clubs_info(t_txt = ('A', 'A', 'C', 'F', 'R', 'S'), title = 'TITLE', output_name = 'image'):

    teams_txt = list()

    for t in t_txt:
        if t == 'Campeão':
            teams_txt.append('C')
        else:
            teams_txt.append(t)
    
    image = Image.open('info6teams.psd')
    img = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=48)

    txt_key = 0
    
    for y in (220, 380):
        for x in (100, 300, 500):
            img.text((x, y), teams_txt[txt_key], font=font, fill='white', anchor='mm')
            txt_key+=1

    img.text((300, 300), title, font=font, fill='white', anchor='mm')

    image.save(f'output\\{output_name}.png', 'png')
    image.close()


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

    image.save(f'output\\{output_name}.png', 'png')
    image.close()


def img_table_6(points=()):
    
    image = Image('tabela6.png')
    img = ImageDraw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=8)

    '''
    points é uma lista/tupla que possui em si a tupla a seguir 6 vezes (uma vez para cada time):
        (id, jogos, vitórias, empates, saldo de gols, gols feitos)
    id = núm. de 0 a 5 que representa a posição do times no ordem alfabética (acre = 0, silvestre = 5)
    '''

    if points == ():

        points = list()

        for pts in range(0, 6):
            points.append((pts, 10, pts, 0, 0, 0))
    
    teams = ('acre', 'amazonense', 'cfc', 'floresta', 'rural', 'silvestre')


if __name__ == '__main__':

    teams_data = read_temp(2022)
    teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')
    comps = dict()

    comps_text = dict()
    comps_text['Acreano'] = (('É CAMPEÃO', 'ACREANO!'), 'Acreano')
    comps_text['Copa Verde'] = (('É CAMPEÃO', 'DA COPA VERDE!'), 'Copa Verde')
    comps_text['Brasileirão'] = (('É CAMPEÃO', 'DA SÉRIE'), 'Brasileirão')
    comps_text['Copa do Brasil'] = (('É CAMPEÃO', 'DA COPA DO BRASIL!'), 'Copa do Brasil')
    comps_text['Sula.'] = (('É CAMPEÃO', 'DA SUL-AMERICANA!'), 'Sul-Americana')
    comps_text['Liberta.'] = (('É CAMPEÃO', 'DA LIBERTADORES!'), 'Libertadores')
    comps_text['Super Copa'] = (('É CAMPEÃO DA', 'SUPERCOPA DO BRASIL!') , 'SuperCopa')
    comps_text['Recopa Sula.'] = (('É CAMPEÃO DA', 'RECOPA SUL-AMERICANA!'), 'Recopa')

    for comp in teams_data['Acre'].keys():
        comps[comp] = list()
        for team in teams_data.keys():
            comps[comp].append(teams_data[team][comp])
    
    comps.pop('Ranking acreano temp.')

    for comp in comps:
        winner = False
        for team in range(0, len(comps[comp])):
            if comps[comp][team] in ('Campeão') or comps[comp][team][0:2] == '1º':
                winner = True
                if comp == 'Brasileirão':
                    serie = f' {comps[comp][team][-2]}!'
                    img_club_info((teams[team], 'confete', 'taça', 'acesso'), (comps_text[comp][0][0], comps_text[comp][0][1]+serie[-2]), f'{teams[team]} campeão {comp}')
                else:
                    img_club_info((teams[team], 'confete', 'taça'), comps_text[comp][0], f'{teams[team]} campeão {comp}')
        img_6clubs_info(comps[comp], comps_text[comp][1].upper(), f'resultados {comp}')

    for team in range(0, 6):
        if int(comps['Brasileirão'][team][:-5]) < 5 and comps['Brasileirão'][team][-2] != 'A':
            img_club_info((teams[team], 'acesso', 'confete'), ('SUBIU DA', f'SÉRIE {comps['Brasileirão'][team][-2]}!'), f'{teams[team]} acesso')

        elif int(comps['Brasileirão'][team][:-5]) > 16 and comps['Brasileirão'][team][-2] != 'C':
            img_club_info((teams[team], 'rebaixado'), ('REBAIXADO', f'DA SÉRIE {comps['Brasileirão'][team][-2]}!'), f'{teams[team]} rebaixado')
        
        elif int(comps['Brasileirão'][team][:-5]) > 16 and comps['Brasileirão'][team][-2] == 'C':
            img_club_info((teams[team], 'rebaixado'), ('VAI FICAR', 'SEM DIVISÃO!'), f'{teams[team]} sem divisão')