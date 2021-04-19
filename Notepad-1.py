from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

root = Tk()
root.title("Notepad-1")

root.resizable(False,False)

def save1():
    L1.config(text=my_text.get(1.0,END))

    '''
    a = (my_text.get(1.0,END))
    print(a)
    '''

def clear():
    my_text.delete(1.0,END)
    L1.config(text="")

def OpenFile():
    text_file = fd.askopenfilename()


menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
edit = Menu(menubar)
form = Menu(menubar)
view = Menu(menubar)
hel = Menu(menubar)

menubar.add_cascade(menu=file,label="File")
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Page Setup")
file.add_command(label="Print")
file.add_command(label="Exit")

menubar.add_cascade(menu=edit,label="Edit")
edit.add_command(label="Undo")
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Find")
edit.add_command(label="Find Next")
edit.add_command(label="Replace")
edit.add_command(label="Go To")
edit.add_command(label="Select All")
edit.add_command(label="Time / Date")

menubar.add_cascade(menu=form,label="Format")
form.add_command(label="Word Wrap")
form.add_command(label="Font")

menubar.add_cascade(menu=view,label="View")
view.add_command(label="Status Bar")

menubar.add_cascade(menu=hel,label="Help")
hel.add_command(label="View Help")
hel.add_command(label="About Notepad")



my_text = Text(root,width=60,height=20,font=("Calibri",12),undo=True)
my_text.grid(row=0,column=0,columnspan=2)

button_frame = Frame(root)
button_frame.grid(row=1,column=0,columnspan=2)

B1 = Button(button_frame,text="Close",command=clear)
B1.grid(row=0,column=0,columnspan=1)
B2 = Button(button_frame,text="Save",command=save1)
B2.grid(row=0,column=1,columnspan=1)
L1 = Label(root,text="")
L1.grid(row=4,column=0,columnspan=2)
B3 = Button(button_frame,text="Redo",command=my_text.edit_redo)
B3.grid(row=1,column=1)
B3 = Button(button_frame,text="Undo",command=my_text.edit_undo)
B3.grid(row=1,column=0)

B4 = Button(button_frame,text="Open file",command=OpenFile)
B4.grid(row=0,column=3)
root.mainloop()