from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Notepad-1")
root.geometry("300x300")
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

T1 = Text(root,wrap="word").pack()

root.mainloop()