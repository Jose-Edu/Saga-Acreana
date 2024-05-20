import tkinter as tk
from tkinter import ttk
import openpyxl as xl


class Application(tk.Frame):
    check = -1


    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.teams = ('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre')
        self.file = xl.load_workbook('Era Fm.xlsx')
        self.sheet = self.file.active = self.file['Clássicos']

        self.create_widgets()


    def create_widgets(self):

        self.cbox1 = ttk.Combobox(self, values=self.teams[0:5])
        self.cbox1.pack(side='left', padx=5, pady=25)
        self.cbox2 = ttk.Combobox(self, values=self.teams)
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

        self.info['cbox1'] = self.cbox1.get()
        self.info['cbox2'] = self.cbox2.get()
        self.info['insert1'] = self.insert1.get()
        self.info['insert2'] = self.insert2.get()

        w_c = True
        loop = self.check

        while w_c:
            for c in range(2, 17):
                if self.sheet[f'D{c}'].value == self.info['cbox1']:
                    line = c
                    break
            for i in range(line, 17):
                if self.sheet[f'G{i}'].value == self.info['cbox2']:
                    line = i
                    break

            self.sheet[f'B{line}'] = self.sheet[f'B{line}'].value + int(self.info['insert1'])
            self.sheet[f'I{line}'] = self.sheet[f'I{line}'].value + int(self.info['insert2'])

            if int(self.info['insert1']) > int(self.info['insert2']):
                add = 'C'
                mg = 'A'
            elif int(self.info['insert1']) < int(self.info['insert2']):
                add = 'H'
                mg = 'J'
            else:
                add = 'E'
            
            self.sheet[f'{add}{line}'] = self.sheet[f'{add}{line}'].value + 1

            if add != 'E':
                if add == 'C':
                    i = '1'
                    c = '2'
                else:
                    i = '2'
                    c = '1'

                game = (int(self.sheet[f'{mg}{line}'].value[0:self.sheet[f'{mg}{line}'].value.find('x')]), int(self.sheet[f'{mg}{line}'].value[self.sheet[f'{mg}{line}'].value.find('x')+1:]))    

                if game[0] - game[1] < int(self.info['insert'+i]) - int(self.info['insert'+c]):
                    self.sheet[f'{mg}{line}'] = f"{int(self.info['insert'+i])}x{int(self.info['insert'+c])}"
                
                elif game[0] - game[1] == int(self.info['insert'+i]) - int(self.info['insert'+c]) and int(self.info['insert'+i]) > game[0]:
                    self.sheet[f'{mg}{line}'] = f"{int(self.info['insert'+i])}x{int(self.info['insert'+c])}"

            if loop == 1:
                loop = -1
                self.sheet = self.file.active = self.file['Clássicos em mata-mata']
            else:
                self.sheet = self.file.active = self.file['Clássicos']
                w_c = False

        self.file.save(filename='Era Fm.xlsx')


    def check_mm_func(self):
        self.check *= -1


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
