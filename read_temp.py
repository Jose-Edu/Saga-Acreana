import openpyxl as xl


def read_temp(temp):

    teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')
    teams_data = dict()
    for c in teams:
        teams_data[c] = dict()

    file = xl.load_workbook('Era Fm.xlsx')
    sheet = file.active = file['Retrospecto times']

    year = str(temp)

    for cell in sheet[1]:
        if year == str(cell.value):
            year_col = cell.column_letter
            break

    for line in range(1, 61):
        if sheet[f'A{line}'].value in teams:
            c_team = sheet[f'A{line}'].value
            continue
        teams_data[c_team][sheet[f'A{line}'].value] = sheet[f'{year_col}{line}'].value
    
    return teams_data