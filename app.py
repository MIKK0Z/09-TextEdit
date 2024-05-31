from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Text editor')
root.geometry('900x600')

def createFile():
    print('create')

def openFile():
    print('open')
    file = filedialog.askopenfile()
    print(file)

def saveFile():
    print('save')

def close():
    print('closing...')
    root.destroy()

def bold():
    print('bold')

def underline():
    print('underline')

def italic():
    print('italic')

# menus
menubar = Menu(root)

# file menu dropdown
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Nowy', command=createFile)
file_menu.add_command(label='Otwórz', command=openFile)
file_menu.add_command(label='Zapisz', command=saveFile)
file_menu.add_command(label='Zamknij', command=close)

menubar.add_cascade(label="File", menu=file_menu)

# edit menu dropdown
edit_menu = Menu(menubar, tearoff=False)
edit_menu.add_command(label='Pogrubienie', command=bold)
edit_menu.add_command(label='Podkreślenie', command=underline)
edit_menu.add_command(label='Pochylenie', command=italic)

# justify submenu
justify_menu = Menu(edit_menu, tearoff=False)
justify_menu.add_command(label='Lewa')
justify_menu.add_command(label='Środek')
justify_menu.add_command(label='Prawa')
edit_menu.add_cascade(label='Wyrównanie', menu=justify_menu)

menubar.add_cascade(label='Edytuj', menu=edit_menu)

root.config(menu=menubar)
root.mainloop()