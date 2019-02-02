import turtle
import math
import random

#Screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.bgpic("bg.gif")
wn.title("Welcome!")
wn.setup (width=550, height=600)
gtnm_shape="gtn.gif"
atel_shape="atl.gif"
wn.addshape(gtnm_shape)
wn.addshape(atel_shape)

#border
border=turtle.Turtle()
border.hideturtle()
border.speed(1000)
border.pensize(3)
border.penup()
border.setposition(-250,-250)
border.pendown()
for i in range (4):
    border.forward(500)
    border.left(90)

#setting gay tanim
gtnm=turtle.Turtle()
gtnm.color("blue")
gtnm.shape(gtnm_shape)
gtnm.penup()
gtnm.speed(0)


#setting atel
atel=turtle.Turtle()
atel.color("red")
atel.shape(atel_shape)
atel.penup()
atel.speed(0)
atel.setposition(random.randint(-220, 220), random.randint(-220, 220))

#setting score and speed
score=0
speed=float(0)
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.speed(500)
def Score ():
    score_pen.undo()
    score_pen.penup()
    score_pen.setposition(-240, 260)
    score_string = "Score: %s" % score
    score_pen.write(score_string, False, align="left", font=("Arial", 14, "bold"))

#start info
start_pen = turtle.Turtle()
start_pen.hideturtle()
start_pen.speed(500)
def StartInfo ():
    start_pen.undo()
    start_pen.penup()
    start_pen.setposition(-50, 260)
    start_string = "Press 'Space' to Start a New Game!"
    start_pen.write(start_string, True, align="left", font=("Arial", 12, "normal"))

#newgame
StartInfo()
def newgame():
    global speed,score
    speed = float(1)
    score = 0
    start_pen.undo()
    gtnm.home()
    atel.setposition(random.randint(-220, 220), random.randint(-220, 220))
    Score()

#move player (Credit:stackoverflow)
wn.onkey(lambda: gtnm.setheading(90), 'Up')
wn.onkey(lambda: gtnm.setheading(180), 'Left')
wn.onkey(lambda: gtnm.setheading(0), 'Right')
wn.onkey(lambda: gtnm.setheading(270), 'Down')
wn.onkey(newgame,"space")
wn.listen()


#player speed and position
while True:
    
    gtnm.forward(speed)

    #check border touch
    if (gtnm.xcor() <= -235 or gtnm.xcor() >= 235):
        speed = float(0)
        StartInfo()
    if (gtnm.ycor() <= -235 or gtnm.ycor() >= 235):
        speed = float(0)
        StartInfo()
    #crashing
    distance=math.sqrt(math.pow(gtnm.xcor() - atel.xcor(), 2) + math.pow(gtnm.ycor() - atel.ycor(), 2))
    #distance --> direct straight line formula xD

    if distance < 30:
        atel.setposition(random.randint(-220, 220), random.randint(-220, 220))
        speed += .1
        score += 5
        #showing score on screen (credit: stackoverflow)
        Score()
