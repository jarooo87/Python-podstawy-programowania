from tkinter import  *
# grid
'''
myWindow = Tk()
myWindow.grid_rowconfigure(0,weight=1)
myWindow.grid_columnconfigure(0,weight=1)
frame = Frame(myWindow)
frame.grid(row=0,column=0,sticky=N+S+E+W)
for row_index in range(5):
    Grid.rowconfigure(frame,row_index,weight=1)
    for col_index in range(10):
        Grid.columnconfigure(frame,col_index,weight=1)
        button = Button(frame)
        button.grid(row=row_index,column=col_index,sticky=N+S+E+W)

myWindow.mainloop()
'''
#progressBar

from tkinter.ttk import *
import time
'''
def start():
    amount = 100
    downloaded = 0
    while(downloaded<amount):
        time.sleep(0.05)
        myPB['value'] += 1
        downloaded +=1
        percents.set(str(int((downloaded/amount)* 100)) + "%")
        isFinished.set(str(downloaded) + " of " + str(amount) + "GB to complete")
        myWindow.update_idletasks()
myWindow = Tk()
percents = StringVar()
isFinished = StringVar()
button = Button(myWindow,text="start downloading",command=start)
button.pack()
myPB = Progressbar(myWindow,length=200,orient=HORIZONTAL,)
myPB.pack()


labelPercent = Label(myWindow,textvariable=percents)
labelPercent.pack()
labelIsFinished = Label(myWindow,textvariable=isFinished)
labelIsFinished.pack()
myWindow.mainloop()
'''
# mouse events
'''
def mouseFunction(event):
    print("Xcor " + str(event.x) + " Ycor " + str(event.y))
myWindow = Tk()
#myWindow.bind("<Button-1>",mouseFunction) left mouse
#myWindow.bind("<Button-2>",mouseFunction) scroll
#myWindow.bind("<Button-3>",mouseFunction) right mouse
#myWindow.bind("<Enter>",mouseFunction)
#myWindow.bind("<Leave>",mouseFunction)
#myWindow.bind("<Motion>",mouseFunction)
myWindow.mainloop()
'''
# key event
def moveUp(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def moveDown(event):
    label.place(x = label.winfo_x(),y = label.winfo_y()+10)
def moveLeft(event):
    label.place(x = label.winfo_x()-10,y = label.winfo_y())
def moveRight(event):
    label.place(x = label.winfo_x()+10,y = label.winfo_y())
myWindow = Tk()
myWindow.geometry("500x500")
myWindow.bind("<Up>",moveUp)
myWindow.bind("<Down>",moveDown)
myWindow.bind("<Left>",moveLeft)
myWindow.bind("<Right>",moveRight)
myPhoto = PhotoImage(file="logo.png")
label = Label(myWindow,image=myPhoto)
label.pack()
myWindow.mainloop()
