import turtle
import random

win =turtle.Screen()
win.title("Giigle Vigilant")
win.bgcolor("black")
win.setup(width=600, height=800)
win.tracer(0)

#Player 

player = turtle.Turtle()
player.shape("turtle")
player.color("orange")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)
player_speed = 30
bullet_speed = 3

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state== "ready":
        bullet_state = "fire"
        x = player.xcor
        y = player.ycor
        bullet.setposition(x,y)
        bullet.swowturtle()

#Controls

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(fire_bullet, "space")
while True:
    win.update()