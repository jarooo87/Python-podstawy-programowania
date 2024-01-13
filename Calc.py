from tkinter import *

def buttonClicked(num):
    global znak
    znak = znak + str(num)
    funkcja_znaku.set(znak)

def buttonEquals():
    global znak
    try:
        wynik = str(eval(znak))
        funkcja_znaku.set(wynik)
        znak = wynik
    except SyntaxError:
        funkcja_znaku.set("Error")
        znak = ""
    except ZeroDivisionError:
        funkcja_znaku.set("Divide by zero")
        znak = ""

def buttonClear():
        global znak
        znak = ""
        funkcja_znaku.set(znak)
def backspace():
        global znak
        cur_text= funkcja_znaku.get()
        funkcja_znaku.set(cur_text[: -1])
        znak =cur_text[:-1]

my_Window = Tk()
my_Window.title("My calculator in Python")
my_Window.geometry("300x400")
znak = ""
funkcja_znaku = StringVar()
label = Label(my_Window,textvariable=funkcja_znaku,font=("Comic Sans",18), bg="white",width=20,height=2)
label.pack()
frame = Frame(my_Window)
frame.pack()
btn1 = Button(frame,text=1,height=2,width=4,font=20,command= lambda: buttonClicked(1))
btn1.grid(row=0,column=0)
btn2 = Button(frame,text=2,height=2,width=4,font=20,command= lambda: buttonClicked(2))
btn2.grid(row=0,column=1)
btn3 = Button(frame,text=3,height=2,width=4,font=20,command= lambda: buttonClicked(3))
btn3.grid(row=0,column=2)
btn4 = Button(frame,text=4,height=2,width=4,font=20,command= lambda: buttonClicked(4))
btn4.grid(row=1,column=0)
btn5 = Button(frame,text=5,height=2,width=4,font=20,command= lambda: buttonClicked(5))
btn5.grid(row=1,column=1)
btn6 = Button(frame,text=6,height=2,width=4,font=20,command= lambda: buttonClicked(6))
btn6.grid(row=1,column=2)
btn7 = Button(frame,text=7,height=2,width=4,font=20,command= lambda: buttonClicked(7))
btn7.grid(row=2,column=0)
btn8 = Button(frame,text=8,height=2,width=4,font=20,command= lambda: buttonClicked(8))
btn8.grid(row=2,column=1)
btn9 = Button(frame,text=9,height=2,width=4,font=20,command= lambda: buttonClicked(9))
btn9.grid(row=2,column=2)
btn0 = Button(frame,text=0,height=2,width=4,font=20,command= lambda: buttonClicked(0))
btn0.grid(row=3,column=1)
btnPlus = Button(frame,text='+',height=2,width=4,font=20,command= lambda: buttonClicked('+'))
btnPlus.grid(row=0,column=3)
btnMinus = Button(frame,text='-',height=2,width=4,font=20,command= lambda: buttonClicked('-'))
btnMinus.grid(row=1,column=3)
btnMultiply = Button(frame,text='*',height=2,width=4,font=20,command= lambda: buttonClicked('*'))
btnMultiply.grid(row=2,column=3)
btnDivide = Button(frame,text='/',height=2,width=4,font=20,command= lambda: buttonClicked('/'))
btnDivide.grid(row=3,column=3)
btnDecimal = Button(frame,text='.',height=2,width=4,font=20,command= lambda: buttonClicked('.'))
btnDecimal.grid(row=3,column=2)
btnEquals = Button(frame,text='=',height=2,width=4,font=20,command= buttonEquals)
btnEquals.grid(row=3,column=0)
btnClear = Button(frame,text='Clear',height=2,width=4,font=20,command= buttonClear)
btnClear.grid(row=4,column=1)
btnBS = Button(frame,text='BS',height=2,width=4,font=20,command= backspace)
btnBS.grid(row=4,column=2)

my_Window.mainloop()