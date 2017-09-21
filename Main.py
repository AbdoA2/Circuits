import tkinter
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.messagebox import askyesno
from CircuitReader import CircuitReaderWriter
from Circuit import Circuit
from dialog import *

class MainWindow(tkinter.Frame):

    def __init__(self, parent):
        self.parent = parent
        self.circuitText = ""
        tkinter.Frame.__init__(self, parent)
        self.createMenus()
        self.createBody()

    def createMenus(self):
        # create the menubar
        menubar = tkinter.Menu(self.parent)

        #create file menu
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Circuit", command=self.new_circuit)
        filemenu.add_command(label="Load Circuit", command=self.load_circuit)
        filemenu.add_separator()
        filemenu.add_command(label="Save Circuit", command=self.save_circuit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)
        menubar.add_cascade(label="File", menu=filemenu)

        # create edit menu
        editmenu = tkinter.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy", command=self.copy)
        editmenu.add_command(label="Cut", command=self.cut)
        editmenu.add_command(label="Paste", command=self.paste)
        editmenu.add_separator()
        editmenu.add_command(label="Find")
        editmenu.add_command(label="Replace")
        menubar.add_cascade(label="Edit", menu=editmenu)

        # create insert menu
        insertmenu = tkinter.Menu(menubar, tearoff=0)
        insertmenu.add_command(label="Voltage Source", command=self.add_element("Voltage Source", "Vsrc"))
        insertmenu.add_command(label="Current Source", command=self.add_element("Current Source", "Isrc"))
        insertmenu.add_separator()
        insertmenu.add_command(label="Resistor", command=self.add_element("Resistor", "R"))
        insertmenu.add_command(label="Capacitor")
        insertmenu.add_command(label="Inductor")
        menubar.add_cascade(label="Insert", menu=insertmenu)

        # create solve menu
        solvemenu = tkinter.Menu(menubar, tearoff=0)
        solvemenu.add_command(label="Solve", command=self.solve_circuit)
        solvemenu.add_command(label="Solve & File", command=self.solve_circuit_file)
        menubar.add_cascade(label="Solve", menu=solvemenu)

        # add the menus to the root window
        self.parent.config(menu=menubar)

    def createBody(self):
        # create the editor texarea
        self.textarea = tkinter.Text(self)
        self.textarea.grid(row=0, column=0, sticky='nsew')
        self.textarea.setvar(self.circuitText)

        # create the answers table
        answers = ttk.Treeview(self)
        answers["columns"] = (0, 1, 2)
        answers.column(0, width=100)
        answers.column(1, width=100)
        answers.column(2, width=100)
        answers.heading(0, text="Voltage")
        answers.heading(1, text="Current")
        answers.heading(2, text="Power")
        answers.grid(row=0, column=1, sticky='nsew')
        self.answers = answers

        # make the elements take all the available space
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

    def load_circuit(self):
        self.new_circuit()
        filename = askopenfilename()
        self.circuitText = open(filename).read()
        self.textarea.insert(tkinter.INSERT, self.circuitText)

    def save_circuit(self):
        f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.textarea.get(1.0, tkinter.END)) # starts from `1.0`, not `0.0`
        f.write(text2save)
        f.close() # `()` was missing.

    def new_circuit(self):
        if len(self.textarea.get("1.0", tkinter.END)) > 2:
            if askyesno('Verify', 'Do you want to save the current circuit?'):
                self.save_circuit()
            else:
                self.textarea.delete("1.0", tkinter.END)

    def copy(self):
        self.textarea.clipboard_clear()
        text = self.textarea.get("sel.first", "sel.last")
        self.textarea.clipboard_append(text)

    def cut(self):
        self.copy()
        self.textarea.delete("sel.first", "sel.last")

    def paste(self):
        text = self.textarea.selection_get(selection='CLIPBOARD')
        self.textarea.insert('insert', text)

    def solve_circuit(self):
        self._solve_circuit()

    def solve_circuit_file(self):
        currents, voltages = self._solve_circuit()
        file = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return

        for k, v in currents.items():
            if type(v) is complex:
                file.write("%s\n%f%+fj %f%+fj %f%+fj\n\n" %
                           (k, voltages[k].real, voltages[k].imag, v.real, v.imag, (voltages[k] * v).real, (voltages[k] * v).imag))
            else:
                file.write("%s\n%.2f %.2f %.2f\n\n" % (k, voltages[k], v, voltages[k] * v))

        file.close()

    def _solve_circuit(self):
        reader = CircuitReaderWriter()
        text2save = str(self.textarea.get(1.0, tkinter.END))
        circuit = reader.parseCircuitFromString(text2save)
        currents, voltages = circuit.getElementsCurrents()
        self.print_solution(currents, voltages)
        return currents, voltages

    def print_solution(self, currents, voltages):
        # clear the current elements if any
        for i in self.answers.get_children():
            self.answers.delete(i)

        for k, v in currents.items():
            self.answers.insert("", 0, text=k, values=(voltages[k], v, v * voltages[k]))

    def insert_element(self, type):
        return lambda values: self.textarea.insert(tkinter.END, type + "_" + " ".join(values) + "\n")

    def add_element(self, name, element):
        return lambda:  ElementDialog(name, self.insert_element(element))

root = tkinter.Tk()
window = MainWindow(root).pack(side="top", fill="both", expand=True)
root.mainloop()