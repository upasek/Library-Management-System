import tkinter
from tkinter import font

import DataBase_connector


class bookRecord:

    def __init__(self, studID):
        self.Stud = studID
        self.BR = tkinter.Frame()
        self.BR.place(x=0, y=0, width=1000, height=700)
        self.BR.config(bg='black')

        label = tkinter.Label(self.BR, text='Student Record', bg='black', fg='white')
        label.grid(row=0, column=0)
        label['font'] = tkinter.font.Font(size=25, family='Helvetica')

        Quit = tkinter.Button(self.BR, text="Quit", pady=10, width=15, activebackground='red', activeforeground='yellow', command=self.BR.destroy)
        Quit.grid(row=2, column=1)

        self.table(self.BR)

        self.BR.rowconfigure(0, weight=1)
        self.BR.rowconfigure(1, weight=4)
        self.BR.rowconfigure(2, weight=1)

        self.BR.columnconfigure(0, weight=4)
        self.BR.columnconfigure(1, weight=1)

        self.BR.mainloop()

    def table(self, root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=50, y=150, width=700, height=500)

        v = tkinter.Scrollbar(labelframe)
        v.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        h = tkinter.Scrollbar(labelframe, orient='horizontal')
        h.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % ('Issue ID', 'Book ID', 'Copy No', 'Issue Date',
                                                                                                       'Issue Staff ID', 'Due Date', 'Is Book Return', 'Return Date',
                                                                                                       'Return Staff ID', 'Fine', 'Is Fine Paid', 'Payment Date',
                                                                                                       'Fine Staff ID'))
        t.insert(tkinter.END, "=" * 250)
        t.insert(tkinter.END, "\n")

        # =================================================
        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT * FROM LibraryManagementSystem.IssuedInfo WHERE studID=%s"
        val = [self.Stud]
        myc.execute(sql, val)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()
        # =================================================

        for i in result:
            t.insert(tkinter.END, "%-15s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s%-20s\n" % (i[0], i[1], i[2], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]))
            t.insert(tkinter.END, "-" * 250)
            t.insert(tkinter.END, "\n")

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        v.config(command=t.yview)
        h.config(command=t.xview)
