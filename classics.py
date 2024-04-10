import tkinter as tk
from tkinter import ttk
import openpyxl as xl


teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')

file = xl.load_workbook('Era Fm.xlsx')
sheet = file.active = file['Clássicos']


class Application(tk.Frame):
    check = -1


    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        global teams

        self.cbox1 = ttk.Combobox(self, values=teams[0:5])
        self.cbox1.pack(side='left', padx=5, pady=25)
        self.cbox2 = ttk.Combobox(self, values=teams)
        self.cbox2.pack(side='right', padx=5, pady=25)

        self.insert1 = tk.Spinbox(self, from_= 0, to=20)
        self.insert1.pack(side='left', padx=5, pady=25)
        self.insert2 = tk.Spinbox(self, from_= 0, to=20)
        self.insert2.pack(side='right', padx=5, pady=25)

        self.check_mm = tk.Checkbutton(self, text='Mata-Mata', command=self.check_mm_func)
        self.check_mm.pack(side='bottom', padx=5, pady=25)

        self.info = dict()
        self.info['cbox1'] = self.cbox1.get()
        self.info['cbox2'] = self.cbox2.get()
        self.info['insert1'] = self.insert1.get()
        self.info['insert2'] = self.insert2.get()
        self.info['check'] = self.check

        self.commit_button = tk.Button(self, text='Commit', command=self.commit)
        self.commit_button.pack(side='bottom', padx=5, pady=25)


    def commit(self):
        global sheet
        global file


        self.info['cbox1'] = self.cbox1.get()
        self.info['cbox2'] = self.cbox2.get()
        self.info['insert1'] = self.insert1.get()
        self.info['insert2'] = self.insert2.get()

        w_c = True
        loop = self.check

        while w_c:
            for c in range(2, 17):
                if sheet[f'D{c}'].value == self.info['cbox1']:
                    line = c
                    break
            for i in range(line, 17):
                if sheet[f'G{i}'].value == self.info['cbox2']:
                    line = i
                    break

            sheet[f'B{line}'] = sheet[f'B{line}'].value + int(self.info['insert1'])
            sheet[f'I{line}'] = sheet[f'I{line}'].value + int(self.info['insert2'])

            if int(self.info['insert1']) > int(self.info['insert2']):
                add = 'C'
                mg = 'A'
            elif int(self.info['insert1']) < int(self.info['insert2']):
                add = 'H'
                mg = 'J'
            else:
                add = 'E'
            
            sheet[f'{add}{line}'] = sheet[f'{add}{line}'].value + 1

            if add != 'E':
                if add == 'C':
                    i = '1'
                    c = '2'
                else:
                    i = '2'
                    c = '1'

                game = (int(sheet[f'{mg}{line}'].value[0:sheet[f'{mg}{line}'].value.find('x')]), int(sheet[f'{mg}{line}'].value[sheet[f'{mg}{line}'].value.find('x')+1:]))    

                if game[0] - game[1] < int(self.info['insert'+i]) - int(self.info['insert'+c]):
                    sheet[f'{mg}{line}'] = f"{int(self.info['insert'+i])}x{int(self.info['insert'+c])}"
                
                elif game[0] - game[1] == int(self.info['insert'+i]) - int(self.info['insert'+c]) and int(self.info['insert'+i]) > game[0]:
                    sheet[f'{mg}{line}'] = f"{int(self.info['insert'+i])}x{int(self.info['insert'+c])}"

            if loop == 1:
                loop = -1
                sheet = file.active = file['Clássicos em mata-mata']
            else:
                sheet = file.active = file['Clássicos']
                w_c = False

        file.save(filename='Era Fm.xlsx')

    def check_mm_func(self):
        self.check *= -1


root = tk.Tk()
app = Application(master=root)
app.mainloop()