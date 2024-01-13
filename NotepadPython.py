import os.path
import tkinter
from tkinter import *
from tkinter import font,colorchooser,filedialog
from tkinter.filedialog import *
from tkinter import messagebox

def font_size_changer(*args):
    first_index = text_field.index(tkinter.SEL_FIRST)
    last_index = text_field.index(tkinter.SEL_LAST)
    rozmiar_czcionki = int(size_box.get())
    nazwa_czcionki = my_font_name.get()
    if rozmiar_czcionki and nazwa_czcionki:
        tags = f"tag{first_index},{last_index}"
        text_field.tag_configure(tags,font=(nazwa_czcionki,rozmiar_czcionki))
        tags_dictionary[tags] = {"rozmiar_czcionki":rozmiar_czcionki,"nazwa_czcionki":nazwa_czcionki}
        text_field.tag_add(tags,first_index,last_index)
def color_changer():
    first_index = text_field.index(tkinter.SEL_FIRST)
    last_index = text_field.index(tkinter.SEL_LAST)
    color = colorchooser.askcolor()
    if color:
        tags =f"tag{len(tags_dictionary) + 1}"
        text_field.tag_configure(tags,foreground= color[1])
        tags_dictionary[tags] = color
        text_field.tag_add(tags,first_index,last_index)


def new_file():
    my_window.title("New file")
    text_field.delete(1.0,END)
def open_file():
    file= askopenfilename(defaultextension=".txt", file =[("All files", "*.*")])
    try:
        my_window.title(os.path.basename(file))
        text_field.delete(1.0, END)
        file = open(file,"r")
        text_field.insert(1.0, file.read())
    except Exception:
        print("Please open another file")
    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile= 'nowy.txt',defaultextension='.txt',file =[("All files", "*.*")])
    try:
        my_window.title(os.path.basename(file))
        file = open(file,"w")
        file.write(text_field.get(1.0,END))
    except Exception:
        print("Can't save file")
    finally:
        file.close()

def copy_file():
    text_field.event_generate("<<Copy>>")
def paste_file():
    text_field.event_generate("<<Paste>>")
def cut_file():
    text_field.event_generate("<<Cut>>")
def info_file():
    messagebox.showinfo("My awesome note", "This is my awesome note created in Python. Version 1.0")
def quit():
    my_window.destroy()

my_window = Tk()
my_window.title("My awesome note")
my_window_width = 500
my_window_height = 500
file = None
scr_width = my_window.winfo_screenwidth()
scr_height = my_window.winfo_screenheight()
x = int((scr_width/2) - (my_window_width/2))
y = int((scr_height/2) - (my_window_height/2))
my_window.geometry("{}x{}+{}+{}".format(my_window_width,my_window_height,x,y))
my_font_size = StringVar(my_window)
my_font_size.set("16")
my_font_name = StringVar(my_window)
my_font_name.set("Calibri")
text_field = Text(my_window,font=(my_font_name.get(), my_font_size.get()))
scroll = Scrollbar(text_field)
text_field.grid(sticky=NSEW)
my_window.grid_rowconfigure(0,weight=1)
my_window.grid_columnconfigure(0,weight=1)
my_frame = Frame(my_window)
my_frame.grid()
font_option = OptionMenu(my_frame,my_font_name, *font.families(), command=font_size_changer)
font_option.grid(row=0,column=0)
size_box = Spinbox(my_frame, from_=1, to=70, textvariable=my_font_size, command=font_size_changer)
size_box.grid(row=0,column=1)
color_button = Button(my_frame,text="color", command=color_changer)
color_button.grid(row=0,column=2)
scroll.pack(side=RIGHT, fill=Y)
text_field.config(yscrollcommand=scroll.set)
tags_dictionary = {}
my_menu = Menu(my_window)
my_window.config(menu=my_menu)
plik_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Plik", menu=plik_menu)
plik_menu.add_command(label ="Nowy", command=new_file)
plik_menu.add_command(label ="Otwórz", command=open_file)
plik_menu.add_command(label ="Zapisz", command=save_file)
plik_menu.add_command(label ="Wyjście", command=quit)
edytuj_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Edycja", menu=edytuj_menu)
edytuj_menu.add_command(label="Kopiuj", command= copy_file)
edytuj_menu.add_command(label="Wklej", command= paste_file)
edytuj_menu.add_command(label="Wytnij",command=cut_file)
info_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Info", menu= info_menu)
info_menu.add_command(label="Informacje",command=info_file)
my_window.mainloop()