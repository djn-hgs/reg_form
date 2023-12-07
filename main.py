import tkinter as tk
from tkinter import ttk


class MyApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create tk variables to store values

        self.name_stringvar = tk.StringVar(self)
        self.email_stringvar = tk.StringVar(self)
        self.gender_stringvar = tk.StringVar(self, value='Female')
        self.country_stringvar = tk.StringVar(self, value='Choose a country')
        self.java_intvar = tk.IntVar(self, value=0)
        self.python_intvar = tk.IntVar(self, value=1)

        # Values for our combo

        country_list = [
            'UK',
            'France',
            'Norway',
            'USA'
        ]

        # Create all our widgets - hopefully the names make it clear what they do!

        self.reg_form_title = tk.Label(self, text='Registration Form')

        self.name_label = tk.Label(self, text='Full name')
        self.name_entry = tk.Entry(self, textvariable=self.name_stringvar)

        self.email_label = tk.Label(self, text='Email')
        self.email_entry = tk.Entry(self, textvariable=self.email_stringvar)

        self.gender_label = tk.Label(self, text='Gender')
        self.gender_radio_male = tk.Radiobutton(self,
                                                text='Male',
                                                variable=self.gender_stringvar,
                                                value='Male'
                                                )
        self.gender_radio_female = tk.Radiobutton(self, text='Female',
                                                  variable=self.gender_stringvar,
                                                  value='Female'
                                                  )

        self.country_label = tk.Label(self, text='Country')
        self.country_combo = ttk.Combobox(self,
                                          values=country_list,
                                          state='readonly',
                                          textvariable=self.country_stringvar
                                          )

        self.programming_label = tk.Label(self, text='Programming')
        self.programming_checkbox_java = tk.Checkbutton(self,
                                                        text='Java',
                                                        variable=self.java_intvar,
                                                        offvalue=0,
                                                        onvalue=1
                                                        )
        self.programming_checkbox_python = tk.Checkbutton(self,
                                                          text='Python',
                                                          variable=self.python_intvar,
                                                          offvalue=0,
                                                          onvalue=1
                                                          )

        self.submit_button = tk.Button(self,
                                       text='Submit',
                                       bg='red',
                                       fg='white'
                                       )



        # Attach our widgets to the grid

        self.reg_form_title.grid(row=0, column=0, columnspan=4, sticky='w', padx=10)

        self.name_label.grid(row=1, column=0, sticky='w', padx=10)
        self.name_entry.grid(row=1, column=1, columnspan=3, sticky='ew', padx=10)

        self.email_label.grid(row=2, column=0, sticky='w', padx=10)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky='ew', padx=10)

        self.gender_label.grid(row=3, column=0, sticky='w', padx=10)
        self.gender_radio_male.grid(row=3, column=1, sticky='w', padx=10)
        self.gender_radio_female.grid(row=3, column=2, sticky='w', padx=10)

        self.country_label.grid(row=4, column=0, sticky='w', padx=10)
        self.country_combo.grid(row=4, column=1, columnspan=2, sticky='ew', padx=10)

        self.programming_label.grid(row=5, column=0, sticky='w', padx=10)
        self.programming_checkbox_java.grid(row=5, column=1, sticky='w', padx=10)
        self.programming_checkbox_python.grid(row=5, column=2, sticky='w', padx=10)

        self.submit_button.grid(row=6, sticky='w', padx=10, pady=10)

        # Describe grid

        self.columnconfigure(index=3, weight=1)

        # Some bindings

        self.country_combo.bind('<<ComboboxSelected>>', self.country_changed)

    def country_changed(self, *args, **kwargs):
        print(self.country_stringvar.get(), args, kwargs)


root = tk.Tk()

my_app = MyApp(root)

my_app.grid(row=0, column=0, sticky='news')

root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)

root.resizable(width=True, height=False)

root.mainloop()
