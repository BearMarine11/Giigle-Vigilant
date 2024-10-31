import turtle
import random

win = turtle.Screen()
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
bullet_speed = 1

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
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#Controls

win.listen()
win.onkey(move_left, "Left")
win.onkey(move_right, "Right")
win.onkey(fire_bullet, "space")

#Player arms

bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.speed(10)
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.hideturtle()
bullet_state ="ready"

#Invanders

num_invaders = 5
invaders = []
for _ in range(num_invaders):
    invader = turtle.Turtle()
    invader.shape("square")
    invader.color("red")
    invader.penup()
    invader.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(100, 250)
    invaders.append(invader)

while True:
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
    win.update()