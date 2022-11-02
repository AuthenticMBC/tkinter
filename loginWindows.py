class windows:
    def __init__(self):
        self.enter = None
        from parameter import parameter
        import tkinter
        from tkinter import StringVar
        self.app = tkinter.Tk()
        self.app.title("WELCOME")
        self.app.geometry(f"{str(parameter.windows_width)}x{str(parameter.windows_height)}")
        self.app.configure(bg="#33b3aa")

        frame = tkinter.Frame(self.app, bg=parameter.whiteColor, width=parameter.main_frame_width,
                              height=parameter.main_frame_height)

        frame_msg = tkinter.Frame(frame, background=parameter.whiteColor)
        msgTxt = "HELLO, WELCOME TO YOUR WORK APPLICATION"
        tkinter.Label(frame_msg, text=msgTxt, font=("Arial", 30), background=parameter.whiteColor, fg="black").pack()

        # display frame_msg
        frame_msg.pack(pady=50)

        # frame_login

        frame_login = tkinter.Frame(frame, background="black")
        msgTxt = "Please enter your username and password to login..."
        tkinter.Label(frame_login, text=msgTxt, background="black", fg="white").grid(pady=20, row=0, column=0)
        tkinter.Label(frame_login, text="Username", background="black", fg="white").grid(row=1, column=0, padx=4)
        self.username = StringVar()
        tkinter.Entry(frame_login, textvariable=self.username, background="black", fg="white").grid(row=1, column=1)

        tkinter.Label(frame_login, text="Password", background="black", fg="white").grid(row=2, column=0, padx=4)
        self.password = StringVar()
        tkinter.Entry(frame_login, textvariable=self.password, background="black", fg="white", show="*").grid(row=2,
                                                                                                              column=1)
        # display frame_login
        frame_login.pack()

        # frame submit

        frame_submit = tkinter.Frame(frame, background="black")
        tkinter.Button(frame_submit, text="Submit", background="black", fg="white", command=self.login).pack(
            expand=True)

        frame_submit.pack(expand=True)
        # display frame

        frame.pack(expand=True)

        # Main loop
        self.app.mainloop()

    def login(self):
        username = self.username.get()
        password = self.password.get()
        data_received = [username, password]
        login_data = [
            ["a", "a"]
        ]
        if data_received in login_data:
            self.switch()


        elif data_received[0] == "" or data_received[1] == "":
            from tkinter import messagebox
            messagebox.showerror("Error", "Sorry ! Please fill your username and your password")

        else:
            from tkinter import messagebox
            messagebox.showerror("Error",
                                 "Sorry, this user doesn't exist ! Please check your input data and try again")

    def switch(self):
        from registrationWindows import registrationWindows
        self.app.destroy()
        registrationWindows()


windows()
