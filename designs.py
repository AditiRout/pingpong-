import turtle
import random

win=turtle.Screen()
win.bgcolor("black")
win.setup(800,800)

lily=turtle.Turtle()

lily.shape("circle")
colors  = ["red","green","blue","orange","purple","pink","yellow","violet","magenta","white","coral"]
for i in range(100):
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    lily.speed(60)
    lily.penup()
    lily.goto(x,y)
    lily.pendown()
    color=random.choice(colors)
    lily.color(color)
    
    for i in range(7):
        lily.forward(100)
        lily.left(60)
    

