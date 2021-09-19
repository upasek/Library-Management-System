import tkinter
import tkinter.font
import DataBase_connector


class viewList:

    def __init__(self):
        self.VB = tkinter.Frame()
        self.VB.place(x=0, y=0, width=1000, height=700)
        self.VB.config(bg='black')

        self.table(self.VB)

        label = tkinter.Label(self.VB, text='List Of Books', bg='black', fg='white')
        label.grid(row=0, column=0)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        quit_b = tkinter.Button(self.VB, text='Quit', command=self.VB.destroy)
        quit_b.grid(row=2, column=1)
        quit_b['font'] = tkinter.font.Font(size=10)

        self.VB.rowconfigure(0, weight=1)
        self.VB.rowconfigure(1, weight=4)
        self.VB.rowconfigure(2, weight=1)

        self.VB.columnconfigure(0, weight=4)
        self.VB.columnconfigure(1, weight=1)

        self.VB.mainloop()

    @staticmethod
    def table(root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=50, y=200, width=800, height=450)

        v = tkinter.Scrollbar(labelframe)
        v.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        h = tkinter.Scrollbar(labelframe, orient='horizontal')
        h.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set, yscrollcommand=v.set)

        # insert some text into the text widget
        t.insert(tkinter.END, "%-15s%-18s%-25s%-20s%-25s%-5s\n" % ('Book ID', 'Title', 'Author', 'Available', 'Total Copies', 'Available Copies'))
        t.insert(tkinter.END, "="*120)
        t.insert(tkinter.END, "\n")

        # ========================================================

        myc = DataBase_connector.my_db.cursor()
        sql = "SELECT BookID, Title, Author, Availability, TotalCopies, Available_copies FROM LibraryManagementSystem.BooksDetails"

        myc.execute(sql)

        result = myc.fetchall()

        DataBase_connector.my_db.commit()

        # ========================================================

        for i in result:
            t.insert(tkinter.END, "%-15s%-18s%-25s%-20s%-25s%-5s\n" % (i[0], i[1], i[2], i[3], i[4], i[5]))
            t.insert(tkinter.END, "-" * 120)
            t.insert(tkinter.END, "\n")

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        v.config(command=t.yview)
        h.config(command=t.xview)
