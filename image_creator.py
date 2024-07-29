import psd_tools as psd_
import os
from PIL import ImageDraw, ImageFont, Image
from read_temp import read_temp


def img_club_info(layers=(), texts=('', ''), output_name='image', path='output\\posts\\'):

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

    image.save(f'{path}{output_name}.png', 'png')
    image.close()


def img_6clubs_info(t_txt = ('A', 'A', 'C', 'F', 'R', 'S'), title = 'TITLE', output_name = 'image', path='output\\posts\\'):

    teams_txt = list()

    for t in t_txt:
        if t == 'Campeão':
            teams_txt.append('C')
        else:
            teams_txt.append(t)
    
    image = Image.open('info6teams.png')
    img = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='ARIBLK.TTF', size=48)

    txt_key = 0
    
    for y in (220, 380):
        for x in (100, 300, 500):
            img.text((x, y), teams_txt[txt_key], font=font, fill='white', anchor='mm')
            txt_key+=1

    img.text((300, 300), title, font=font, fill='white', anchor='mm')

    image.save(f'{path}{output_name}.png', 'png')
    image.close()


def img_tumb(teams=('Acre', 'Silvestre'), comp='Copa', fase='8/F', output_name='image', path='output\\posts\\', title_size=128):

    psd = psd_.PSDImage.open('tumb.psd')

    layer_var = list(filter(lambda layer: layer.name == teams[0]+'_e', psd.descendants()))[0]
    layer_var.visible = True

    if teams[1] in ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre'):
        layer_var = list(filter(lambda layer: layer.name == teams[1]+'_d', psd.descendants()))[0]
        layer_var.visible = True
        image = psd.composite(force=True)
    else:
        image = psd.composite(force=True)
        img = Image.open(f'escudos//{teams[1]}.png')
        size = sorted((img.height, img.width))[1]
        img_n = Image.new('RGBA', (size, size), (0, 0, 0, 0))

        place_img = [(sorted((img.height, img.width))[1]-sorted((img.height, img.width))[0])//2, 0]
        for i in place_img: 
            if i < 0: i = 0

        img_n.paste(img, place_img, img)
        img_n = img_n.resize((480, 480))
        image.paste(img_n, (1300, 280), img_n)
        img_n.close()

    img = ImageDraw.Draw(image)

    font = ImageFont.truetype(font='ARIBLK.TTF', size=title_size)
    img.text((960, 166), f'{teams[0]} x {teams[1]}'.upper(), font=font, fill='white', anchor='mm')
    font = ImageFont.truetype(font='ARIBLK.TTF', size=72)
    img.text((960, 276), comp, font=font, fill='white', anchor='mm')
    img.text((960, 358), fase, font=font, fill='white', anchor='mm')

    image.save(f'{path}{output_name}.png', 'png')
    image.close()


def img_table_6(points=(), order=range(6), round=10, path='output\\posts\\'):

    '''
    points é uma lista/tupla que possui em si a tupla a seguir 6 vezes (uma vez para cada time):
        (id, jogos, vitórias, empates, saldo de gols, gols feitos)
    id = núm. de 0 a 5 que representa a posição do times no ordem alfabética (acre = 0, silvestre = 5)

    order é uma tupla/lista que define a ordem de exibição dos times (id de 0 a 5 para os times)
    '''

    if points == ():

        points = list()

        for pts in range(0, 6):
            points.append([pts, 10, pts, pts, 0, 0])
    
    for team in points:
        team.append(team[2]*3+team[3])

    image = Image.open('tabela6.png')
    line = 0
    font = ImageFont.truetype('ARIBLK.TTF', 26)
    teams = ('acre', 'amazonense', 'cfc', 'floresta', 'rural', 'silvestre')

    for index, team in enumerate(order):
        img = Image.open(f'escudos//{teams[team]}.png')
        img = img.resize((50, 50))
        image.paste(img, (106, 215+63*line), img)
        col = 0
        for crit in (1, 6, 2, 3, 4, 5):
            img = ImageDraw.Draw(image)
            txt = '0' + str(points[index][crit]) if points[index][crit] < 10 else str(points[index][crit])
            img.text((184+67*col, 221+63*line), txt, fill='white', font=font)
            col += 1

        line += 1
    
    image.save(f'{path}tabela acreano {round}.png', 'png')


def img_table_4(comp, points, sub='Grupo A', path='output\\posts\\'):
    '''
    points é uma lista/tupla que possui em si a tupla a seguir 4 vezes (uma vez para cada time):
        (nome, jogos, vitórias, empates, saldo de gols, gols feitos)
    '''
    
    for team in points:
        team.append(team[2]*3+team[3])

    image = Image.open('tabela4.png')
    line = 0
    font = ImageFont.truetype('ARIBLK.TTF', 26)

    for index in range(4):
        img = Image.open(f'escudos//{points[index][0]}.png')

        size = sorted((img.height, img.width))[1]
        img_n = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        place_img = [(sorted((img.height, img.width))[1]-sorted((img.height, img.width))[0])//2, 0]
        for i in place_img: 
            if i < 0: i = 0
        img_n.paste(img, place_img, img)
        img_n = img_n.resize((50, 50))

        image.paste(img_n, (106, 255+87*line), img_n)
        img_n.close()
        col = 0
        for crit in (1, 6, 2, 3, 4, 5):
            img = ImageDraw.Draw(image)
            txt = '0' + str(points[index][crit]) if points[index][crit] < 10 else str(points[index][crit])
            img.text((184+67*col, 260+87*line), txt, fill='white', font=font)
            col += 1

        line += 1
    
    font = ImageFont.truetype('ARIBLK.TTF', 58)
    img_draw = ImageDraw.Draw(image)
    img_draw.text((300, 40), comp, 'white', font, 'mm')
    font = ImageFont.truetype('ARIBLK.TTF', 48)
    img_draw.text((300, 100), sub, 'white', font, 'mm')

    image.save(f'{path}{comp} {sub}.png', 'png')


def main(season):
    teams_data = read_temp(season)
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

    path = os.path.dirname(__file__) + '//output//posts//'

    for comp in comps:
        for team in range(0, len(comps[comp])):
            if comps[comp][team] in ('Campeão') or comps[comp][team][0:2] == '1º':
                if comp == 'Brasileirão':

                    serie = f' {comps[comp][team][-2]}!'
                    out = path+f'end//campeão br {serie}'
                    os.mkdir(out)

                    with open(out+'//text.txt', 'w') as text:
                        text.write(f'O {teams[team]} é o campeão brasileiro da Série {serie}!')

                    img_club_info((teams[team], 'confete', 'taça', 'acesso'), (comps_text[comp][0][0], comps_text[comp][0][1]+serie), f'{teams[team]} campeão {comp}', out+'//')

                else:
                    out = path+f'during//campeão {comp}'
                    os.mkdir(out)

                    with open(out+'//text.txt', 'w') as text:
                        text.write(f'O {teams[team]} '+comps_text[comp][0][0].lower()+' '+comps_text[comp][0][1].lower())

                    img_club_info((teams[team], 'confete', 'taça'), comps_text[comp][0], f'{teams[team]} campeão {comp}', out+'//')
        
        name = f'resultados {comp}'
        out = path+f'during//'+name
        os.mkdir(out)

        with open(out+'//text.txt', 'w') as text:
            text.write(f'Resultados finais do(a) {comp}')

        img_6clubs_info(comps[comp], comps_text[comp][1].upper(), name, out+'//')

    for team in range(0, 6):
        if int(comps['Brasileirão'][team][:-5]) < 5 and comps['Brasileirão'][team][-2] != 'A':
            name = f'{teams[team]} acesso'
            out = path+'end//'+name
            os.mkdir(out)
            
            with open(out+'//text.txt', 'w') as text:
                text.write(f'O {teams[team]} subiu da Série {comps['Brasileirão'][team][-2]}!')

            img_club_info((teams[team], 'acesso', 'confete'), ('SUBIU DA', f'SÉRIE {comps['Brasileirão'][team][-2]}!'), name, out+'//')

        elif int(comps['Brasileirão'][team][:-5]) > 16 and comps['Brasileirão'][team][-2] != 'C':
            name = f'{teams[team]} rebaixado'
            out = path+'end//'+name
            os.mkdir(out)
            
            with open(out+'//text.txt', 'w') as text:
                text.write(f'O {teams[team]} foi rebaixado da Série {comps['Brasileirão'][team][-2]}!')

            img_club_info((teams[team], 'rebaixado'), ('REBAIXADO', f'DA SÉRIE {comps['Brasileirão'][team][-2]}!'), name, out+'//')
        
        elif int(comps['Brasileirão'][team][:-5]) > 16 and comps['Brasileirão'][team][-2] == 'C':
            name = f'{teams[team]} sem divisão'
            out = path+'end//'+name
            os.mkdir(out)
            
            with open(out+'//text.txt', 'w') as text:
                text.write(f'O {teams[team]} foi rebaixado da Série C do Brasileirão! O {teams[team]} está sem divisão para a próxima temporada!')

            img_club_info((teams[team], 'rebaixado'), ('VAI FICAR', 'SEM DIVISÃO!'), name, out+'//')


if __name__ == '__main__':
    main(input('Digite o ano para criar as imagens'))
