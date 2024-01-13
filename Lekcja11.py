# tkinter
from tkinter import *
'''
myWindow = Tk()
myWindow.geometry("400x400")
myWindow.resizable(FALSE,FALSE)
myWindow.title("My first window")
icon = PhotoImage(file="logo.png")
myWindow.iconphoto(True,icon)
myWindow.config(background= '#25b08d')
myWindow.mainloop()
'''
# label etykieta
'''
myWindow = Tk()
photo = PhotoImage(file='logo.png')
label = Label(myWindow,text="Moja etykieta",font=('Comic Sans',20,'bold'),fg="blue",
              bg="green",relief=RAISED,bd=40,image=photo,compound='bottom')
label.pack()
#label.place(x=100,y=50)
myWindow.mainloop()
'''
'''
# przyciski buttons
licznik = 0
def enterButton():
    global licznik
    while licznik < 100000:
        licznik += 1
        print(licznik)

myWindow = Tk()
photo = PhotoImage(file='logo.png')
button = Button(myWindow,text='enter',fg='blue',bg='black',
                activebackground='black',font=("Comic Sans",20),
                command=enterButton,state=ACTIVE,image=photo,
                compound='top')
button.pack()
myWindow.mainloop()
'''
# entryBox
def click():
    data = entry.get()
    print(data)
def delete():
    entry.delete(0,END)
myWindow = Tk()
entry = Entry(myWindow,font=('Arial',30),fg='blue',bg='yellow',
              )
entry.insert(0,"Wpisz swoje imie")
entry.pack(side='left')
clickButton = Button(myWindow,text='wyslij',command=click,
                     compound='top')
clickButton.pack(side='right')
delButton = Button(myWindow,text='usun',command=delete)
delButton.pack(side='right')
myWindow.mainloop()