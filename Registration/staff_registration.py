import tkinter
from PIL import Image, ImageTk
from tkinter import font

import DataBase_connector


class Registration_A:
    def __init__(self):
        self.root = tkinter.Frame()
        self.root.place(x=0, y=0, width=1000, height=700)
        self.root.config(bg='black')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img, width=250, height=150)
        panel.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img2, width=250, height=150)
        panel.grid(row=0, column=2)

        label = tkinter.Label(self.root, text='Staff Registration', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        self.name = tkinter.Label(self.root, text='Name', bg='black', fg='white')
        self.name.grid(row=1, column=1, sticky='W')
        self.name['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.name_entry = tkinter.Entry(self.root)
        self.name_entry.grid(row=1, column=1, sticky='E')

        self.mobile_no = tkinter.Label(self.root, text='Mobile No.', bg='black', fg='white')
        self.mobile_no.grid(row=2, column=1, sticky='W')
        self.mobile_no['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.mobile_no_entry = tkinter.Entry(self.root)
        self.mobile_no_entry.grid(row=2, column=1, sticky='E')

        self.email = tkinter.Label(self.root, text='Email ID', bg='black', fg='white')
        self.email.grid(row=3, column=1, sticky='W')
        self.email['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.email_entry = tkinter.Entry(self.root)
        self.email_entry.grid(row=3, column=1, sticky='E')

        self.Staff_ID = tkinter.Label(self.root, text='Staff ID', bg='black', fg='white')
        self.Staff_ID.grid(row=4, column=1, sticky='W')
        self.Staff_ID['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.Staff_ID_entry = tkinter.Entry(self.root)
        self.Staff_ID_entry.grid(row=4, column=1, sticky='E')

        self.__password = tkinter.Label(self.root, text='Password', bg='black', fg='white')
        self.__password.grid(row=5, column=1, sticky='W')
        self.__password['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.__password_entry = tkinter.Entry(self.root)
        self.__password_entry.grid(row=5, column=1, sticky='E')

        cancel = tkinter.Button(self.root, text='Cancel', pady=10, width=20, activebackground='red', activeforeground='yellow', command=self.root.destroy)
        cancel.grid(row=6, column=0)
        cancel['font'] = tkinter.font.Font(size=10)

        register = tkinter.Button(self.root, text='Register', pady=10, width=20, activebackground='red', activeforeground='yellow', command=self.checkInfo)
        register.grid(row=6, column=2)
        register['font'] = tkinter.font.Font(size=10)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)

        self.root.mainloop()

    def checkInfo(self):
        if self.name_entry.get() and self.mobile_no_entry.get() and self.email_entry.get() and self.Staff_ID_entry.get() and self.__password_entry.get():

            try:
                myc = DataBase_connector.my_db.cursor()
                sql = "INSERT INTO LibraryManagementSystem.StaffLoginInfo(staff_name, mobile_no, email_ID, staff_ID, s_password) VALUES(%s, %s, %s, %s, %s)"
                val = [self.name_entry.get(), self.mobile_no_entry.get(), self.email_entry.get(),
                       self.Staff_ID_entry.get(), self.__password_entry.get()]

                myc.execute(sql, val)

                DataBase_connector.my_db.commit()

                self.successful()

            except ValueError:
                window = tkinter.Tk()
                window.title("Library Management System")
                window.geometry("300x100-530-250")
                window.config(bg="black")
                window["pady"] = 15

                label = tkinter.Label(window, text="Please enter correct Info!", bg="black", fg='white')
                label.pack()

                window.minsize(300, 100)
                window.maxsize(300, 100)

                window.after(2500, window.destroy)

                window.mainloop()

        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-250")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter all information.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def successful(self):
        self.Swindow = tkinter.Tk()
        self.Swindow.title("Library Management System")
        self.Swindow.geometry("300x100-530-250")
        self.Swindow.config(bg="black")
        self.Swindow['pady'] = 20

        label = tkinter.Label(self.Swindow, text='Registration Successful!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.Swindow, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.Swindow.minsize(300, 100)
        self.Swindow.maxsize(300, 100)

        # self.window.after(2500, self.window.destroy)

        self.Swindow.mainloop()

    def refresh(self):
        self.Swindow.destroy()
        self.root.destroy()
