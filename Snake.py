import turtle
import time
import random
my_window = turtle.Screen()
my_window.title("My Snake Game in Python")
my_window.bgcolor("black")
my_window.setup(width=500,height=500)
snake_head = turtle.Turtle()
snake_head.speed(1)
snake_head.shape("square")
snake_head.color("red")
snake_head.goto(0,0)
snake_head.penup()
snake_head.direction = "stop"


def snake_move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y -20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x -20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
def snake_up():
    if snake_head.direction != "down":
     snake_head.direction = "up"
def snake_down():
    if snake_head.direction != "up":
     snake_head.direction = "down"
def snake_left():
    if snake_head.direction != "right":
     snake_head.direction = "left"
def snake_right():
    if snake_head.direction != "left":
     snake_head.direction = "right"
def quit():
    global running
    running = False

my_window.listen()
my_window.onkeypress(snake_up,"w")
my_window.onkeypress(snake_down,"s")
my_window.onkeypress(snake_left,"a")
my_window.onkeypress(snake_right,"d")
my_window.onkeypress(quit,"q")
food = turtle.Turtle()
food.shape("circle")
food.speed(0)
food.color("green")
food.penup()
food.goto(40,40)
body = []
my_score = 0
high_score = 0
table_score = turtle.Turtle()
table_score.speed(0)
table_score.shape("square")
table_score.color("white")
table_score.penup()
table_score.hideturtle()
table_score.goto(0,200)
table_score.write("My score:0 High score:0",align= "center",font=("Arial",20,"normal"))
running = True
while running:
 try:

  my_window.update()
  snake_move()
  for a in body:
      if a.distance(snake_head) < 20:
          time.sleep(1)
          snake_head.goto(0,0)
          snake_head.direction = "stop"
          for a in body:
              a.goto(600,600)
          body.clear()
          my_score =0
          table_score.clear()
          table_score.write("Score: {} High Score {}".format(my_score,high_score),align="center",font=("Arial",20,"normal"))
  time.sleep(0.25)
  if snake_head.distance(food) < 20:
      x = random.randint(-6,6)
      y = random.randint(-6,6)

      food.goto(x * 20, y * 20)
      new_body = turtle.Turtle()
      new_body.shape("square")
      new_body.color("blue")
      new_body.speed(0)
      new_body.penup()
      body.append(new_body)

      my_score +=1
      if my_score > high_score:
          high_score = my_score
      table_score.clear()
      table_score.write("Score: {} High Score {}".format(my_score, high_score), align="center",
                        font=("Arial", 20, "normal"))
  for index in range(len(body)-1,0,-1):
      x = body[index -1].xcor()
      y = body[index -1].ycor()
      body[index].goto(x,y)
  if len(body) > 0:
      x = snake_head.xcor()
      y = snake_head.ycor()
      body[0].goto(x,y)
  if snake_head.xcor() > 235 or snake_head.xcor() < -235 or snake_head.ycor() > 235 or snake_head.ycor() < -235:
      time.sleep(1)
      snake_head.goto(0,0)
      snake_head.direction = "stop"
      for a in body:
          a.goto(600,600)
      body.clear()
      my_score = 0
      table_score.clear()
      table_score.write("Score: {} High Score {}".format(my_score, high_score), align="center",
                        font=("Arial", 20, "normal"))

 except turtle.Terminator:
  break

my_window.mainloop()