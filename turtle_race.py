import turtle
import random
import time

###### Set up the Welcome Screen ######

t1 = turtle.Turtle()
t1.penup()
t1.goto(0,0)
t1.pendown()
t1.color('red')
t1.write('Welcome to Turtle Race',align='center',font=('arial',20))
t1.hideturtle()

wn = turtle.Screen()

def screen_set():
  global wn
  wn.title('Turtle Race')
  wn.clear()
  wn.bgcolor('green2')

  return wn

###### Creating Racers ######

def place_competitors():
  
  all_turtle = []
  x = -180
  y = 180
  colors = ['red','blue','green','magenta','pink','cyan','brown','yellow','skyblue','orange']

  for i in range(10):
    i = turtle.Turtle()
    i.speed(20)
    i.begin_fill()
    i.color(random.choice(colors))
    i.shape('turtle')
    i.end_fill()
    i.penup()
    i.goto(x,y)
    i.pendown()
    all_turtle.append(i)
    y=y-40
    
  return all_turtle

###### Drawing Finish Line ######

def finish_line():
  
  f = turtle.Turtle()
  f.speed(0)
  f.penup()
  f.goto(155,185)
  f.pendown()
  f.right(90)
  
  for i in range(38):
    f.begin_fill()
    if i%2!=0:
      for j in range(4):
        f.forward(10)
        f.left(90)
        f.fillcolor('black')
    else:
      for j in range(4):
        f.forward(10)
        f.left(90)
        f.fillcolor('white')
    f.end_fill()
    f.forward(10)
  
  f.hideturtle() 
  return f

###### Main Race ######

def race():
  
  screen_set()
  finish_line()
  all_turtle = place_competitors()
  
  is_on = True
  while is_on:
    for turtle in all_turtle:
      random_pace = random.randint(1,10)
      x1 = turtle.xcor()+random_pace
      y1=turtle.ycor()
      distance = turtle.xcor()
      y1 = turtle.ycor()
      winner = (x1/100) - 1
      if (distance>149):
        is_on=False
        turtle.penup()
        turtle.goto(x1+15,y1)
        turtle.color('black')
        turtle.write('winner',font=('arial',20,'bold'))
        turtle.hideturtle()
        time.sleep(1)
      turtle.goto(x1,y1)

###### Taking Input To start Play ######

answer = wn.textinput("Prompt", "Strat/Play Again?")

if answer.lower() == 'yes' or answer.lower() == 'y':
  race()
  s = turtle.Turtle()
  s.color('black')
  screen_set()
  s.write('GAME OVER!',align='center',font=('arial',30,'bold'))
  s.hideturtle()
  time.sleep(3)
  
  while True:
    
    answer = wn.textinput("Prompt", "Strat/Play Again?")
    
    if answer.lower()=='no' or answer.lower()=='n':
      screen_set()
      d = turtle.Turtle()
      d.color('black')
      d.write('Thanks For Coming',align='center',font=('arial',30,'bold'))
      d.hideturtle()
      break
    else:
      race()
      s = turtle.Turtle()
      s.color('black')
      s.write('GAME OVER!',align='center',font=('arial',30,'bold'))
      s.hideturtle()
      time.sleep(1)

else:
  screen_set()
  d = turtle.Turtle()
  d.color('black')
  d.write('Thanks For Coming',align='center',font=('arial',30,'bold'))
  d.hideturtle()

turtle.done()
