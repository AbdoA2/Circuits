from tkinter import Entry, Label, Tk, Frame, Button

class ElementDialog(Frame):
    def __init__(self, type, callback):
        self.root = Tk()
        Frame.__init__(self, self.root)
        self.pack(side="top", fill="both", expand=True)
        self.type = type
        self.callback = callback
        self.createBody()
        self.root.mainloop()

    def createBody(self):
        Label(self, text="New:").grid(row=0, column=0)
        Label(self, text=self.type).grid(row=0, column=1)
        Label(self, text="ID").grid(row=1, column=0)
        Label(self, text="Positive Node").grid(row=2, column=0)
        Label(self, text="Negative Node").grid(row=3, column=0)
        Label(self, text="Value").grid(row=4, column=0)
        self.id = Entry(self)
        self.id.grid(row=1, column=1)
        self.posNode = Entry(self)
        self.posNode.grid(row=2, column=1)
        self.negNode = Entry(self)
        self.negNode.grid(row=3, column=1)
        self.value = Entry(self)
        self.value.grid(row=4, column=1)
        if self.type == "Voltage Source" or self.type == "Current Source":
            Label(self, text="Phase").grid(row=5, column=0)
            self.phase = Entry(self)
            self.phase.grid(row=5, column=1)
        Button(self, text="Insert", command=self.return_element).grid(row=6, column=0)
        Button(self, text="Cancel", command=self.root.destroy).grid(row=6, column=1)

    def return_element(self):
        values = [self.id.get(), "v" + self.posNode.get(), "v" + self.negNode.get(), self.value.get()]
        if self.type == "Voltage Source" or self.type == "Current Source" and self.phase.get() != "":
            values += [self.phase.get()]
        self.callback(values)
        self.root.destroy()
