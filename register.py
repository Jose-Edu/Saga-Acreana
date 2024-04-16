import openpyxl as xl

teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')
teams_data = dict()
for c in teams:
    teams_data[c] = dict()

file = xl.load_workbook('Era Fm.xlsx')
sheet = file.active = file['Retrospecto times']

year = input('Digite o ano de registro: ')

for cell in sheet[1]:
    if year == str(cell.value):
        year_col = cell.column_letter
        break

for line in range(1, 61):
    if sheet[f'A{line}'].value in teams:
        c_team = sheet[f'A{line}'].value
        continue
    teams_data[c_team][sheet[f'A{line}'].value] = sheet[f'{year_col}{line}'].value

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