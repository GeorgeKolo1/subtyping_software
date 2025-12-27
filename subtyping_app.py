import customtkinter
from customtkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

    
        self.title('my app')
        self.geometry('1000x1000')
        self.grid_columnconfigure((0,1), weight=1)

        checkbox_1 = customtkinter.CTkCheckBox(self, text='Tickbox1', command=self.checkbox_callback)
        checkbox_1.grid(row=1, column=0, padx=20, pady=(0,20), sticky='w', columnspan=2)
        checkbox_2 = customtkinter.CTkCheckBox(self, text='Tickbox2', command=self.checkbox_callback2)
        checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='w', columnspan=2)

        button = customtkinter.CTkButton(self, text='Press?', command=self.button_callback)
        button.grid(row=0, padx=20, pady=20, sticky='ew')
        

        
    
    def button_callback(self):
        print('YIPEEEEEEE')

    def checkbox_callback(self):
        print('Wow')

    def checkbox_callback2(self):
        print('lol')
    
    def optionmenu_callback(self):
        print('lol')

app = App()
app.mainloop()
