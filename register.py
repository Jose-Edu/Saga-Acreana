import openpyxl as xl
from read_temp import read_temp

# region pontuação geral
teams_data = read_temp(input('Digite o ano a ser registrado'))

file = xl.load_workbook('Era Fm.xlsx')
sheet = file.active = file['Pontuação geral']

comp_cols =  {

    'Liberta.': 'D',
    'Copa do Brasil': 'F',
    'Sula.': 'G',
    'Recopa Sula.': 'H',
    'Super Copa': 'I',
    'Copa Verde': 'K',
    'Acreano': 'L',

}

for line in range(3, 9):
    for comp in teams_data[sheet[f'A{line}'].value]:
        try:
            if teams_data[sheet[f'A{line}'].value][comp] == 'Campeão':
                sheet[f'{comp_cols[comp]}{line}'] = sheet[f'{comp_cols[comp]}{line}'].value + 1
            elif teams_data[sheet[f'A{line}'].value][comp] == '1º [A]':
                sheet[f'E{line}'] = sheet[f'E{line}'].value + 1
            elif teams_data[sheet[f'A{line}'].value][comp] == '1º [B]':
                sheet[f'J{line}'] = sheet[f'J{line}'].value + 1
            elif teams_data[sheet[f'A{line}'].value][comp] == '1º [C]':
                sheet[f'M{line}'] = sheet[f'M{line}'].value + 1
        except:
            continue

for line in range(12, 18):
    team = sheet[f'A{line}'].value
    
    if teams_data[team]['Copa do Brasil'] not in ('1ª fase', '2ª fase'):
        sheet[f'G{line}'] = sheet[f'G{line}'].value + 1
    
    if teams_data[team]['Copa Verde'] != 'F.G':
        sheet[f'H{line}'] = sheet[f'H{line}'].value + 1
    
    if teams_data[team]['Brasileirão'] != '-':
        br = teams_data[team]['Brasileirão'][teams_data[team]['Brasileirão'].find('[')+1]
    
    try:
        if br == 'A':
            sheet[f'I{line}'] = sheet[f'I{line}'].value + 1
        elif br == 'B':
            sheet[f'J{line}'] = sheet[f'J{line}'].value + 1
        elif br == 'C':
            sheet[f'K{line}'] = sheet[f'K{line}'].value + 1
    except:
        sheet[f'L{line}'] = sheet[f'L{line}'].value + 1

    if teams_data[team]['Liberta.'] != '-':
        sheet[f'E{line}'] = sheet[f'E{line}'].value + 1
    
    if teams_data[team]['Sula.'] != '-':
        sheet[f'F{line}'] = sheet[f'F{line}'].value + 1

file.save('Era Fm.xlsx')
file.close()
# endregion

# region tabela temp
file = xl.load_workbook('temporada.xlsx')
sheet = file.active

comps = [x for x in teams_data['Acre'].keys()]
comps.remove('Ranking acreano temp.')

for col in 'BCDEFG':

    line = 2

    for comp in comps:
        try:
            sheet[f'{col}{line}'] = teams_data[sheet[f'{col}1'].value][comp]
        finally:
            line += 1
        
file.save('temporada_saída.xlsx')
file.close()
# endregion