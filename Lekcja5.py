import myModule
myModule.mojaFunkcja1()
myModule.mojaFunkcja2('Andrzej')

from turtle import *

#rysujemy kwadrat, komendy:forward(),left(),right()
# color('red'),pensize(zmieniamy grubosc),
# exitonclick() - rysunek zostaje po wykonaniu programu
# hideturtle()
'''
color('blue')
pensize(5)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
hideturtle()
exitonclick()
'''
# rysujemy trojkat
'''
color('red')
forward(110)
left(120)
forward(110)
left(120)
forward(110)
color('blue')
left(120)
forward(110)
left(120)
forward(110)
left(120)
forward(110)
hideturtle()
exitonclick()
'''
# komendy: begin_fill(), end_fill() - wypelnianie ksztaltu
# circle(na ile pikseli), penup(), pendown(), goto(x,y)
# yellow circle
'''
penup()
goto(-150,130)
pendown()
color('yellow')
begin_fill()
circle(30)
end_fill()
# red circle
penup()
goto(0,-100)
pendown()
color('red')
begin_fill()
circle(50)
end_fill()
hideturtle()
exitonclick()
'''
# petle for
'''
color('red')
left(90)
begin_fill()
for i in range(5):
    forward(150)
    left(144)
end_fill()
hideturtle()
exitonclick()
'''
# powiekszenie za pomoca petli for
'''
def draw():
    size = 10
    for i in range(6):
        circle(size)
        size += 10
speed(2)
color('blue')
for i in range(4):
    draw()
    left(90)
hideturtle()
exitonclick()
'''
# operatory warunkowe if
'''
def green():
    color('green')
    begin_fill()
    circle(50)
    end_fill()
def red():
    color('red')
    begin_fill()
    circle(50)
    end_fill()

age = int(input("Tell me your age:"))
if age < 18:
    red()
elif age >= 18:
    green()
hideturtle()
exitonclick()
'''
def redLightOn():
    color('red')
    penup()
    goto(0,150)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
def redLightOff():
    color('red')
    penup()
    goto(0,150)
    pendown()
    circle(50)

def yellowLightOn():
    color('yellow')
    penup()
    goto(0,0)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
def yellowLightOff():
    color('yellow')
    penup()
    goto(0,0)
    pendown()
    circle(50)
def greenLightOn():
    color('green')
    penup()
    goto(0,-150)
    pendown()
    begin_fill()
    circle(50)
    end_fill()
def greenLightOff():
    color('green')
    penup()
    goto(0,-150)
    pendown()
    circle(50)
answer = input('Give me color of lights (red/yellow/green):')
if answer == 'red':
    redLightOn()
    yellowLightOff()
    greenLightOff()
elif answer == 'yellow':
    redLightOff()
    yellowLightOn()
    greenLightOff()
elif answer == 'green':
    redLightOff()
    yellowLightOff()
    greenLightOn()

hideturtle()
exitonclick()





