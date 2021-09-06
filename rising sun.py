import turtle

win=turtle.Screen()
win.bgcolor("black")
win.setup(600,600)

sun=turtle.Turtle()
sun.shape("circle")
sun.color("gold")
sun.penup()
sun.goto(0,0)
sun.pendown()
sun.speed(100)
for i in range(50):
    sun.forward(200)
    sun.left(180)
    sun.forward(200)
    sun.left(40)

sun.goto(0,0)
sun.begin_fill()
sun.circle(5)
sun.end_fill()

ray=turtle.Turtle()
ray.hideturtle()
ray.speed(100)
ray.penup()
ray.goto(200,0)
ray.pendown()
ray.color("gold")
for i in range(50):
    ray.right(100)
    ray.forward(200)
    ray.right(80)
    ray.forward(400)
    ray.right(80)
    ray.forward(200)

ray.penup()
ray.goto(200,0)
ray.pendown()

for i in range(50):
    ray.left(100)
    ray.forward(200)
    ray.left(80)
    ray.forward(400)
    ray.left(80)
    ray.forward(200)
    
    
    
