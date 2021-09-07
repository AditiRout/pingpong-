import turtle
import random
import math

win=turtle.Screen()
win.bgcolor("black")
win.setup(600,600)

lily=turtle.Turtle()
lily.shape("triangle")
lily.penup()
lily.speed(70)
lily.goto(0,0)
lily.pendown()

lil=turtle.Turtle()
lil.shape("triangle")
lil.speed(70)



rose=turtle.Turtle()
rose.penup()
rose.goto(0,-100)
rose.pendown()
rose.pensize(30)
rose.color("white")
rose.circle(100)
rose.speed(70)


colors=["white","blue","orange","brown","red","sky blue","navy blue","violet","purple","magenta","sea green","yellow","lime green"]

for i in range(75):
    col=random.choice(colors)
    lily.color(col)
    lily.penup()
    lily.setheading(-5*i+20)
    lily.forward(100)
    lily.stamp()
    lily.penup()
    lily.backward(100)
lily.hideturtle()
for i in range(75):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    lil.goto(x,y)
    col=random.choice(colors)
    lil.color(col)
    lil.penup()
    lil.setheading(-20*i+20)
    lil.forward(10)
    lil.stamp()
    lil.penup()
