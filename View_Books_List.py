import tkinter
import tkinter.font


class viewList:

    def __init__(self):
        self.VB = tkinter.Frame()
        self.VB.place(x=0, y=0, width=1000, height=700)
        self.VB.config(bg='black')

        self.table(self.VB)

        label = tkinter.Label(self.VB, text='List Of Books', bg='black', fg='white')
        label.grid(row=0, column=1)
        label['font'] = tkinter.font.Font(size=30, family='Helvetica')

        quit_b = tkinter.Button(self.VB, text='Quit', command=self.VB.destroy)
        quit_b.grid(row=2, column=2)
        quit_b['font'] = tkinter.font.Font(size=10)

        self.VB.rowconfigure(0, weight=1)
        self.VB.rowconfigure(1, weight=1)
        self.VB.rowconfigure(2, weight=1)

        self.VB.columnconfigure(0, weight=1)
        self.VB.columnconfigure(1, weight=1)
        self.VB.columnconfigure(2, weight=1)

        self.VB.mainloop()

    def table(self, root):
        labelframe = tkinter.Frame(root, bg='black')
        labelframe.place(x=250, y=200, width=500, height=400)

        h = tkinter.Scrollbar(labelframe)
        h.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        t = tkinter.Text(labelframe, width=15, height=30, wrap=tkinter.NONE, xscrollcommand=h.set)

        # insert some text into the text widget
        t.insert(tkinter.END, "%-15s%-15s%-15s%-10s\n" % ('Book ID', 'Title', 'Author', 'availability'))
        t.insert(tkinter.END, "=========================================================================\n")
        for i in range(200):
            t.insert(tkinter.END, "this is some text\n", i)

        t.pack(side=tkinter.TOP, fill=tkinter.X)

        h.config(command=t.yview)

        # t = tkinter.Text(root)
        #
        # x = PrettyTable()
        # x.border = True
        # x.field_names = ['Book ID', 'Title', 'Author', 'num']
        #
        # x.add_row([1, 'Raj', 'Mumbai', 19])
        # x.add_row([2, 'Aaryan', 'Pune', 18])
        # x.add_row([3, 'Vaishnavi', 'Mumbai', 20])
        # x.add_row([4, 'Rachna', 'Mumbai', 21])
        # x.add_row([5, 'Shubham', 'Delhi', 21])
        #
        # x.align['num'] = 'r'
        #
        # t.insert(tkinter.INSERT, x)
        # t.grid(row=1, column=1)
