# colorChooser
from tkinter import *
from tkinter import colorchooser
'''
def choose():
    a = colorchooser.askcolor()
    print(a)
    myWindow.config(bg =a[1])
myWindow = Tk()
myWindow.geometry("500x500")
button = Button(myWindow,text="press",command=choose)
button.pack()
myWindow.mainloop()
'''
# text area
'''
def sending():
    a = text.get("1.0",END)
    print(a)
myWindow = Tk()
text = Text(myWindow)
text.pack()
button = Button(myWindow,text="click",command=sending)
button.pack()
myWindow.mainloop()
'''
# open a file ( filedialog)
from tkinter import  filedialog
'''
def opening():
    a = filedialog.askopenfilename()
    myFile = open(a,'r')
    print(myFile.read())
    myFile.close()
myWindow = Tk()
button = Button(myWindow,text="open",command= opening)
button.pack()
myWindow.mainloop()
'''
'''
# saving file
def saving():
    a = filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("text type",".txt")],initialdir="C:\\Users\\jaros\\PycharmProjects\\programowaniePythonsemestrI")
    b = str(text.get("1.0",END))
    a.write(b)
    a.close()

myWindow = Tk()
text = Text(myWindow)

text.pack()
button = Button(myWindow,text="save",command=saving)
button.pack()
myWindow.mainloop()
'''
from tkinter import messagebox
# messagebox
def msg():
    #messagebox.showinfo(title="Information",message="Here is some msg"
    #while(True):
     #messagebox.showwarning(title="Virus",message="Installing virus..please wait")
     #messagebox.showerror(title="Error", message="Some type of error!")
     #if messagebox.askyesno(title="yesno",message="Do you like it?"):
          #print("ok you like it")
      #else:
          #print(("DONT"))
      #messagebox.askokcancel(title="ask",message="Are you sure??")
      yourChoice = messagebox.askquestion(title="ask",message="Do you like it")
      if(yourChoice == 'yes'):
            print("You like it")
      else:
            print("DONT")

myWindow = Tk()
button = Button(myWindow,text="click",command=msg)
button.pack()
myWindow.mainloop()