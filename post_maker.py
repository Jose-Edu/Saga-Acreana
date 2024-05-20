from tkinter.filedialog import askopenfiles
from os import mkdir
from os.path import dirname
from shutil import copy


# region texts
texts = dict()

texts['br_'] = 'O Campeonato Brasileiro chegou à §ª rodada!'

texts['vgs'] = 'Realizado o sorteio da Fase de Grupos da Copa Verde!'
texts['vfg'] = 'A fase de grupos da Copa Verde chegou à §ª rodada!'
texts['v4s'] = 'Confrontos definidos para as Quartas-de-Final da Copa Verde!'
texts['v4r'] = 'Resultados das Quartas-de-Final da Copa Verde!'
texts['v2s'] = 'Confrontos definidos para as Semifinais da Copa Verde!'
texts['v2r'] = 'Resultados das Semifinais da Copa Verde!'

texts['cfs'] = 'Sorteados os confrontos para a §ª fase da Copa do Brasil!'
texts['cfr'] = 'Resultados da §ª fase da Copa do Brasil!'
texts['c8s'] = 'Confrontos definidos para as Oitavas-de-Final da Copa do Brasil!'
texts['c8r'] = 'Resultados das Oitavas-de-Final da Copa do Brasil!'
texts['c4s'] = 'Confrontos definidos para as Quartas-de-Final da Copa do Brasil!'
texts['c4r'] = 'Resultados das Quartas-de-Final da Copa do Brasil!'
texts['c2s'] = 'Confrontos definidos para as Semifinais da Copa do Brasil!'
texts['c2r'] = 'Resultados das Semifinais da Copa do Brasil!'

texts['acr'] = 'O Campeonato Acreano chegou à §ª rodada!'
texts['acf'] = 'A final do Campeonato Acreano está definida!'

texts['ssg'] = 'Realizado o sorteio da Fase de Grupos da Sul-Americana!'
texts['sfg'] = 'A fase de grupos da Sul-Americana chegou à §ª rodada!'
texts['s8s'] = 'Confrontos definidos para as Oitavas-de-Final da Sul-Americana!'
texts['s8r'] = 'Resultados das Oitavas-de-Final da Sul-Americana!'
texts['s4s'] = 'Confrontos definidos para as Quartas-de-Final da Sul-Americana!'
texts['s4r'] = 'Resultados das Quartas-de-Final da Sul-Americana!'
texts['s2s'] = 'Confrontos definidos para as Semifinais da Sul-Americana!'
texts['s2r'] = 'Resultados das Semifinais da Sul-Americana!'

texts['lsg'] = 'Realizado o sorteio da Fase de Grupos da Libertadores!'
texts['lfg'] = 'A fase de grupos da Libertadores chegou à §ª rodada!'
texts['l8s'] = 'Confrontos definidos para as Oitavas-de-Final da Libertadores!'
texts['l8r'] = 'Resultados das Oitavas-de-Final da Libertadores!'
texts['l4s'] = 'Confrontos definidos para as Quartas-de-Final da Libertadores!'
texts['l4r'] = 'Resultados das Quartas-de-Final da Libertadores!'
texts['l2s'] = 'Confrontos definidos para as Semifinais da Libertadores!'
texts['l2r'] = 'Resultados das Semifinais da Libertadores!'

texts['rjg'] = 'Estatísticas da partida do dia'
# endregion


def main(txt=None):

    global texts

    files = askopenfiles()
    paths = list()
    file_name = list()

    for cont, path in enumerate(files):
        paths.append(path.name)
        file_name.append(paths[cont][paths[cont].rfind('/')+1:])

    code = file_name[0][:5]
    post_type = 'end' if code == 'br_38' else 'during'
    path = dirname(__file__)+f'//output//posts//{post_type}//{code}'
    mkdir(path)
    code = (code[0:3], code[3:])

    with open(path+'//text.txt', 'w') as text:
        if txt is None:
            text.write(texts[code[0]].replace('§', code[1]))
        else:
            text.write(txt)
    
    for file in paths:
        copy(file, path)


if __name__ == '__main__':
    main()
