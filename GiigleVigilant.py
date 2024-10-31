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

while True:
    win.update()