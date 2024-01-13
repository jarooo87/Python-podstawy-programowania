# checkBox // checkButton
from tkinter import *
'''
def show():
    if(a.get() == 1):
        print("chechButton clicked!")
    else:
        print("Please click the chechButton")
myWindow = Tk()
photo = PhotoImage(file='logo.png')
a = IntVar()
checkButton = Checkbutton(myWindow,text="confirm",font=('Arial',25),
                          padx= 50,pady=50,variable=a,onvalue=1,
                          offvalue=0,command=show,image=photo)
checkButton.pack()
myWindow.mainloop()
'''
'''
# radiobutton
def choose():
    if(a.get() == 0):
        print("You chose Audi")
    elif(a.get() == 1):
        print("You chose Honda")
    else:
        print("You chose Citroen")
cars = ["Audi","Honda","Citroen"]
myWindow = Tk()
photo1 = PhotoImage(file='logo.png')
photo2 = PhotoImage(file='logo.png')
photo3 = PhotoImage(file='logo.png')
photos = [photo1,photo2,photo3]
a = IntVar(value=3)
for i in range(len(cars)):
    radioBtn = Radiobutton(myWindow,text=cars[i],variable=a,
                           value=i,pady=50,padx=50,command=choose,
                           image=photos[i])
    radioBtn.pack()
myWindow.mainloop()
'''
#listbox
def sending():
    try:
        print(lista.get(lista.curselection()))
    except(Exception):
        print("You have to choose smth")

def adding():
    lista.insert(lista.size(),entry.get())
    lista.config(height=lista.size())
def deleting():
    lista.delete(lista.curselection())
    lista.config(height=lista.size())
myWindow = Tk()
lista = Listbox(myWindow,bg='yellow',font=("Comic Sans",25),width=10)
lista.pack()
lista.insert(1,"marchew")
lista.insert(2,"kapusta")
lista.insert(3,"banany")
lista.insert(4,"arbuz")
lista.config(height=lista.size())
entry = Entry(myWindow)
entry.pack()
sendButton = Button(myWindow,text="send",command=sending)
sendButton.pack()
addButton = Button(myWindow,text="add",command=adding)
delButton = Button(myWindow,text="delete",command=deleting)
delButton.pack()
addButton.pack()

myWindow.mainloop()