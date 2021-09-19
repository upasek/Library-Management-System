import tkinter
from tkinter import font
from PIL import Image, ImageTk

import DataBase_connector


class update_profile:
    def __init__(self, studID):
        self.name_entry = None
        self.mobile_no_entry = None
        self.email_entry = None
        self.stud_id_entry = None
        self.val_b = studID

        # ====================
        myc = DataBase_connector.my_db.cursor()

        sql = "SELECT * FROM LibraryManagementSystem.StudentLoginInfo WHERE student_ID = %s"
        val = [self.val_b]

        myc.execute(sql, val)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()

        # ====================

        self.root = tkinter.Frame()
        self.root.place(x=0, y=0, width=1000, height=700)
        self.root.config(bg='black')

        img = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img, width=250, height=150)
        panel.grid(row=0, column=0)

        img2 = ImageTk.PhotoImage(Image.open('Images/lib1.jpeg'))
        panel = tkinter.Label(self.root, image=img2, width=250, height=150)
        panel.grid(row=0, column=2)

        label = tkinter.Label(self.root, text='Update Details', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        self.name = tkinter.Label(self.root, text='Name', bg='black', fg='white')
        self.name.grid(row=1, column=1, sticky='W')
        self.name['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.name_entry = tkinter.Entry(self.root)
        self.name_entry.insert(0, result[0][1])
        self.name_entry.grid(row=1, column=1, sticky='E')

        self.mobile_no = tkinter.Label(self.root, text='Mobile No.', bg='black', fg='white')
        self.mobile_no.grid(row=2, column=1, sticky='W')
        self.mobile_no['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.mobile_no_entry = tkinter.Entry(self.root)
        self.mobile_no_entry.insert(0, result[0][2])
        self.mobile_no_entry.grid(row=2, column=1, sticky='E')

        self.email = tkinter.Label(self.root, text='Email ID', bg='black', fg='white')
        self.email.grid(row=3, column=1, sticky='W')
        self.email['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.email_entry = tkinter.Entry(self.root)
        self.email_entry.insert(0, result[0][3])
        self.email_entry.grid(row=3, column=1, sticky='E')

        self.stud_id = tkinter.Label(self.root, text='Student ID', bg='black', fg='white')
        self.stud_id.grid(row=4, column=1, sticky='W')
        self.stud_id['font'] = tkinter.font.Font(size=15, family='Helvetica')
        self.stud_id_entry = tkinter.Entry(self.root)
        self.stud_id_entry.insert(0, result[0][4])
        self.stud_id_entry.grid(row=4, column=1, sticky='E')

        cancel = tkinter.Button(self.root, text='Cancel', pady=10, width=20, activebackground='red',
                                activeforeground='yellow', command=self.root.destroy)
        cancel.grid(row=6, column=0)
        cancel['font'] = tkinter.font.Font(size=10)

        update = tkinter.Button(self.root, text='Update', pady=10, width=20, activebackground='red',
                                activeforeground='yellow', command=self.update_DB)
        update.grid(row=6, column=2)
        update['font'] = tkinter.font.Font(size=10)

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

    def update_DB(self):
        if self.name_entry.get() and self.mobile_no_entry.get() and self.email_entry.get() and self.stud_id_entry.get():
            self.UpdateFromDB()
        else:
            window = tkinter.Tk()
            window.title("Library Management System")
            window.geometry("300x100-530-400")
            window.config(bg="black")
            window['pady'] = 5

            label = tkinter.Label(window, text="WARNING!", bg='black', fg='white')
            label.pack(side='top')
            label['font'] = tkinter.font.Font(size=15, family='Helvetica', weight='bold')

            label2 = tkinter.Label(window, text='Please Enter All Information.', bg='black', fg='white')
            label2.pack(side='top')

            # ok button for destroy frame
            ok = tkinter.Button(window, text="OK", activebackground='#FFA500',
                                command=window.destroy)
            ok.pack(side='bottom', anchor='n')
            ok['font'] = tkinter.font.Font(size=15)

            window.minsize(300, 100)
            window.maxsize(300, 100)
            window.mainloop()

    def UpdateFromDB(self):
        myc = DataBase_connector.my_db.cursor()

        sql = "UPDATE LibraryManagementSystem.StudentLoginInfo SET student_name = %s, mobile_no = %s, email_ID = %s, student_ID = %s WHERE (student_ID = %s AND sr_no <> %s)"
        val = (str(self.name_entry.get()), str(self.mobile_no_entry.get()), str(self.email_entry.get()), str(self.stud_id_entry.get()), str(self.val_b), 0)

        myc.execute(sql, val)

        DataBase_connector.my_db.commit()

        self.successful()

    def successful(self):
        self.Swindow = tkinter.Tk()
        self.Swindow.title("Library Management System")
        self.Swindow.geometry("300x100-530-250")
        self.Swindow.config(bg="black")
        self.Swindow['pady'] = 20

        label = tkinter.Label(self.Swindow, text='Information Updated Successfully!', bg="black", fg='white')
        label.pack()

        ok = tkinter.Button(self.Swindow, text="OK", activebackground='#FFA500',
                            command=self.refresh)
        ok.pack(side='bottom', anchor='n')
        ok['font'] = tkinter.font.Font(size=15)

        self.Swindow.minsize(300, 100)
        self.Swindow.maxsize(300, 100)

        self.Swindow.mainloop()

    def refresh(self):
        self.Swindow.destroy()
        self.root.destroy()
