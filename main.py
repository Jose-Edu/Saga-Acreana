import image_creator, classics, post_maker, register, video_editor
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox


class App(ttk.Frame):


    def __init__(self, master=None) -> None:
        
        # Call Tk init
        super().__init__(master)
        self.pack()

        # Set window basic attributes
        self.master = master
        self.master.resizable(False, False)
        self.master.title('Saga Acreana App')

        # Notebook set
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # region Notebook tabs

        # region Register

        self.tab_register = ttk.Frame(self.notebook)
        self.tab_register.pack(fill='both', expand=True)
        self.notebook.add(self.tab_register, text='Register')

        ttk.Label(self.tab_register, text='Write the year to Full Register:', font=('Arial', 26)).pack(pady=25)

        self.entry_rg_year = ttk.Entry(self.tab_register)
        self.entry_rg_year.pack(pady=25, padx=25, fill='x')

        ttk.Button(self.tab_register, text='Full Register', command=self.full_register).pack()

        # endregion

        # region Classics

        self.tab_classics = ttk.Frame(self.notebook)
        self.tab_classics.pack(fill='both', expand=True)
        self.notebook.add(self.tab_classics, text='Classics')

        classics.Application(self.tab_classics)

        # endregion

        # region Post Maker

        self.tab_post_maker = ttk.Frame(self.notebook)
        self.tab_post_maker.pack(fill='both', expand=True)
        self.notebook.add(self.tab_post_maker, text='Post Maker')

        ttk.Label(self.tab_post_maker, text='Click on the button to make a post', font=('Arial', 26)).pack(pady=25)
        ttk.Button(self.tab_post_maker, text='Make a post', command=self.mk_post, width=100).pack()

        # endregion

        # region Image Creator

        self.tab_image_creator = ttk.Frame(self.notebook)
        self.tab_image_creator.pack(fill='both', expand=True)
        self.notebook.add(self.tab_image_creator, text='Image Creator')

        ttk.Label(self.tab_image_creator, text='Choose the image template:', font=('Arial', 26)).pack(pady=15)

        ttk.Button(self.tab_image_creator, text='Club info', command=self.imgcr_club_info).pack(pady=10)
        ttk.Button(self.tab_image_creator, text='All clubs info', command=self.imgcr_all_clubs_info).pack(pady=10)
        ttk.Button(self.tab_image_creator, text='Tumbnail 2 teams', command=self.imgcr_tumb_2teams).pack(pady=10)
        ttk.Button(self.tab_image_creator, text='Table 6', command=self.imgcr_table_6).pack(pady=10)

        # endregion

        # endregion


    def full_register(self) -> None:

        try:
            year = int(self.entry_rg_year.get())
        except ValueError:
            msgbox.showerror('ERROR', 'ERROR: Please, input a year as a integer number format.')
        else:
            image_creator.main(year)
            register.main(year)
            video_editor.main()
            msgbox.showinfo('SUCCESS!', f'SUCCESS INFO: The season of {year} was Full Registered successfully!')


    def mk_post(self) -> None:
        post_maker.main()


    def imgcr_club_info(self) -> None:

        
        def create():
            layers = list()

            for layer in self.img_ci_checkbuttons.keys():
                if self.img_ci_checkbuttons[layer].get() == 1:
                    layers.append(layer)
            
            layers.append(self.img_ci_cbox_teams.get())

            texts = (self.img_ci_text1.get(), self.img_ci_text2.get())

            image_creator.img_club_info(layers, texts)
            msgbox.showinfo('SUCCESS!', 'SUCCESS INFO: Image created successfully!')


        self.tab_img_club_info = ttk.Frame(self.notebook)
        self.tab_img_club_info.pack(fill='both', expand=True)
        self.notebook.add(self.tab_img_club_info, text='Image Creator: Club Info')

        self.img_ci_checkbuttons = dict()
        self.img_ci_checkbuttons['confete'] = tk.IntVar()
        self.img_ci_checkbuttons['taça'] = tk.IntVar()
        self.img_ci_checkbuttons['rebaixado'] = tk.IntVar()
        self.img_ci_checkbuttons['acesso'] = tk.IntVar()

        self.img_ci_confete = ttk.Checkbutton(self.tab_img_club_info, text='confete', variable=self.img_ci_checkbuttons['confete'])
        self.img_ci_taca = ttk.Checkbutton(self.tab_img_club_info, text='taça', variable=self.img_ci_checkbuttons['taça'])
        self.img_ci_rebaixado = ttk.Checkbutton(self.tab_img_club_info, text='rebaixado', variable=self.img_ci_checkbuttons['rebaixado'])
        self.img_ci_acesso = ttk.Checkbutton(self.tab_img_club_info, text='acesso', variable=self.img_ci_checkbuttons['acesso'])
        self.img_ci_confete.pack()
        self.img_ci_taca.pack()
        self.img_ci_rebaixado.pack()
        self.img_ci_acesso.pack()

        self.img_ci_text1 = ttk.Entry(self.tab_img_club_info)
        self.img_ci_text2 = ttk.Entry(self.tab_img_club_info)
        self.img_ci_text1.pack()
        self.img_ci_text2.pack()

        self.img_ci_cbox_teams = ttk.Combobox(self.tab_img_club_info, values=('Acre', 'Amazonense', 'C.F.C', 'Floresta', 'Rural', 'Silvestre'), state='readonly')
        self.img_ci_cbox_teams.pack()

        ttk.Button(self.tab_img_club_info, text='Create', command=create).pack()


    def imgcr_all_clubs_info(self) -> None: #todo
        
        self.tab_img_all_clubs_info = ttk.Frame(self.notebook)
        self.tab_img_all_clubs_info.pack(fill='both', expand=True)
        self.notebook.add(self.tab_img_all_clubs_info, text='Image Creator: All Clubs Info')


    def imgcr_tumb_2teams(self) -> None: #todo

        self.tab_img_tumb_2teams = ttk.Frame(self.notebook)
        self.tab_img_tumb_2teams.pack(fill='both', expand=True)
        self.notebook.add(self.tab_img_tumb_2teams, text='Image Creator: Tumbnail 2Teams')


    def imgcr_table_6(self) -> None: #todo

        self.tab_img_table6 = ttk.Frame(self.notebook)
        self.tab_img_table6.pack(fill='both', expand=True)
        self.notebook.add(self.tab_img_table6, text='Image Creator: Table 6')


if __name__ == '__main__':

    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
