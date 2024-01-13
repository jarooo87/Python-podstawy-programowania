# skala
from tkinter import *
'''
def showScale():
    print("This is your value: " + str(scale.get()))

myWindow = Tk()
somePhoto = PhotoImage(file="logo.png")
label = Label(image=somePhoto)
label.pack()
scale = Scale(myWindow,from_=0,to=159,length=500,orient=VERTICAL,
              font=("Comic Sans",20),tickinterval=20,resolution=20,
              troughcolor='green',fg='blue',bg='yellow')
scale.pack()
button = Button(myWindow,text="click",command=showScale)
button.pack()
myWindow.mainloop()
'''
#menu
'''
def opening():
    print("open a file")
def saving():
    print("save a file")
def copying():
    print("Copy a file")
def pasting():
    print("Paste a file")
def cutting():
    print(("Cut text"))
myWindow = Tk()
myPhoto = PhotoImage(file="logo.png")
myMenu = Menu(myWindow)
myWindow.config(menu=myMenu)
fileMenu = Menu(myMenu,font=("Comic Sans",20),tearoff=0)
myMenu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command= opening,image=myPhoto,compound="right")
fileMenu.add_separator()
fileMenu.add_command(label="Save",command= saving)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command= quit)

editMenu = Menu(myMenu,font=("Comic Sans",20),tearoff=0)
myMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Copy", command= copying)
editMenu.add_separator()
editMenu.add_command(label="Paste", command= pasting)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=cutting)
myWindow.mainloop()
'''
'''
# frames , new window
def opening():
    #myNewWindow = Toplevel()
      myNewWindow = Tk()
      myWindow.destroy()
myWindow = Tk()
frame = Frame(myWindow,bg='blue')
frame.pack()
button1 = Button(frame,text="open",font=("Arial",20),command=opening)
button1.pack(side=TOP)
button2 = Button(frame,text="1",font=("Arial",20))
button2.pack(side=LEFT)
button3 = Button(frame,text="2",font=("Arial",20))
button3.pack(side=LEFT)
button4 = Button(frame,text="3",font=("Arial",20))
button4.pack(side=LEFT)
myWindow.mainloop()
'''
# tags zakladki
from tkinter import ttk
myWindow = Tk()
myNote = ttk.Notebook(myWindow)
myTab1 = Frame(myNote)
myTab1.pack()
myTab2 = Frame(myNote)
myTab1.pack()
myNote.add(myTab1,text='tab1')
myNote.add(myTab2,text='tab2')
myNote.pack(expand=True,fill='both')
label1 = Label(myTab1,text="here is place for tab1", width=50,height=50)
label1.pack()
label2 = Label(myTab2,text="here is place for tab2",width=50,height=50)
label2.pack()

myWindow.mainloop()