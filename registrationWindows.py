class registrationWindows:
    def __init__(self):
        # create the windows of the registration form
        # ------ Windows Config ------
        import tkinter
        from tkinter import StringVar
        from parameter import parameter
        self.windows = tkinter.Tk()
        self.windows.title("REGISTRATION FORM")
        self.windows.geometry(f"{str(parameter.windows_width)}x{str(parameter.windows_height)}")
        self.windows.configure(bg="#33b3aa")

        # ------ Frame Registration form ------

        frame = tkinter.Frame(self.windows, bg=parameter.whiteColor, width=parameter.main_frame_width,
                              height=parameter.main_frame_height)

        # text : Registration form...
        self.entry_list = []
        txt_frame01 = tkinter.Frame(frame)
        label_01 = tkinter.Label(txt_frame01, text="Registration Form", bg=parameter.whiteColor, font=("Arial", 30),
                                 fg="#33b3aa")
        label_01.pack()
        txt_frame01.pack(pady=50)

        # frame02
        frame02 = tkinter.Frame(frame)

        # Name
        name_frame = tkinter.Frame(frame02)
        name = tkinter.Label(name_frame, text="Name")
        self.var_entry_name = StringVar()
        entry_name = tkinter.Entry(name_frame, textvariable=self.var_entry_name)
        self.entry_list.append(entry_name)
        name.grid(row=0, column=0, padx=2)
        entry_name.grid(row=0, column=1)
        name_frame.grid(pady=5, row=0, column=0)

        # Surname
        surname_frame = tkinter.Frame(frame02)
        surname = tkinter.Label(surname_frame, text="Surname")
        self.var_entry_surname = StringVar()
        entry_surname = tkinter.Entry(surname_frame, textvariable=self.var_entry_surname)
        self.entry_list.append(entry_surname)
        surname.grid(row=0, column=0, padx=2)
        entry_surname.grid(row=0, column=1)
        surname_frame.grid(pady=5, row=0, column=1)
        # email
        email_frame = tkinter.Frame(frame02)
        email = tkinter.Label(email_frame, text="Email address")
        self.var_entry_email = StringVar()
        entry_email = tkinter.Entry(email_frame, textvariable=self.var_entry_email)
        self.entry_list.append(entry_email)
        email.grid(row=0, column=0, padx=2)
        entry_email.grid(row=0, column=1, padx=2)
        email_frame.grid(pady=5, row=1, column=0)

        # Phone Number
        phone_frame = tkinter.Frame(frame02)
        phone = tkinter.Label(phone_frame, text="Phone number")
        self.var_entry_phone = StringVar()
        entry_phone = tkinter.Entry(phone_frame, textvariable=self.var_entry_phone)
        self.entry_list.append(entry_phone)
        phone.grid(row=0, column=0, padx=2)
        entry_phone.grid(row=0, column=1, padx=2)
        phone_frame.grid(pady=5, row=1, column=1)

        # Nationality
        nationality_frame = tkinter.Frame(frame02)
        nationality = tkinter.Label(nationality_frame, text="Nationality")
        self.var_entry_nationality = StringVar()
        entry_nationality = tkinter.Entry(nationality_frame, textvariable=self.var_entry_nationality)
        self.entry_list.append(entry_nationality)
        nationality.grid(row=0, column=0, padx=2)
        entry_nationality.grid(row=0, column=1, padx=2)
        nationality_frame.grid(pady=5, row=4)

        # display frame02
        frame02.pack(pady=5)
        # submit button
        btn_frame = tkinter.Frame(frame)
        btn_submit = tkinter.Button(btn_frame, text="Submit Informations", command=self.save_data)
        btn_submit.pack()
        btn_frame.pack()

        # display Frame
        frame.update_idletasks()
        frame.pack(expand=True)

        # Python terminal

        # ------ MAIN LOOP  ------
        self.windows.mainloop()

    def getLastRows(self):  # get the last row of the Excel file database

        from get_rows_columns import get_row_column

        numRows = get_row_column("registered_database.xls", 'sheet1')[0]
        lastRow = numRows
        return lastRow

    def get_password_id(self):
        import pickle
        with open('password_id', 'rb') as rb:
            list_password_id = pickle.load(rb)
        return list_password_id

    def save_data(self):  # save the information of the registration form in the Excel file
        from tkinter import messagebox
        list_password_id = self.get_password_id()

        name = self.var_entry_name.get().lower().capitalize()

        surname = self.var_entry_surname.get().lower().capitalize()

        email = self.var_entry_email.get()

        phone = self.var_entry_phone.get()

        nationality = self.var_entry_nationality.get().lower().capitalize()

        if name == "" and email == "" and nationality == "" and phone == "":
            msg = "Sorry ! You didn't complete all the information's required,  please refill the form and try again !"
            messagebox.showerror("Missing info", msg)
        else:
            try:
                phonestr = phone.replace(" ", "")
                phone = int(phonestr)
                if len(phonestr) < 15:
                    choice = messagebox.askquestion("Send Information ?", "Final state ! You sure with those data ?")
                    if choice == 'yes':
                        import tkinter
                        import xlrd
                        from xlutils.copy import copy
                        password_id = list_password_id[0]
                        messagebox.showinfo(title="Your id Password", message=f"Password : {password_id}")
                        list_password_id = list_password_id[1:]
                        list_data = [name, surname, email, phone, nationality, password_id]
                        # keys = [i[0] for i in data.keys()]
                        data = {"name": name,
                                "surname": surname,
                                "email": email,
                                "phone": phone,
                                "nationality": nationality,
                                "password": password_id}

                        rb = xlrd.open_workbook("registered_database.xls", formatting_info=True)
                        r_sheet = rb.sheet_by_index(0)
                        wb = copy(rb)
                        w_sheet = wb.get_sheet(0)
                        for i in range(len(list_data)):
                            lastRow = self.getLastRows()
                            w_sheet.write(lastRow, i, list_data[i])

                        # lastRow += 1
                        print(data)
                        wb.save("registered_database.xls")
                        print(f"Personals information of {self.var_entry_name.get()} have been successfully saved...")

                        """entry_name.delete(0, tkinter.END)
                        entry_email.delete(0, tkinter.END)
                        entry_nationality.delete(0, tkinter.END)"""

                        for entry in self.entry_list:
                            entry.delete(0, tkinter.END)
                else:
                    msg = "Sorry ! A phone number can't have more than 15 digits, please correct it..."
                    messagebox.showerror("Phone Number", msg)
            except:
                msg = "Sorry ! The phone number entered is not correct ! please correct it"
                messagebox.showerror("Phone", msg)
