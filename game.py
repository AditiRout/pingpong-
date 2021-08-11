import turtle

win = turtle.Screen()
win.title("pong game")
win.setup(800,600)
win.bgcolor("black")
win.tracer(0)

paddle=turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("limegreen")
paddle.shapesize(stretch_wid=1,stretch_len=10)
paddle.penup()
paddle.goto(0,-260)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

score=0

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:0",align="center",font=("Arial",24,"normal"))
def goLeft():
    x=paddle.xcor()
    x-=100
    paddle.setx(x)
def goRight():
    x = paddle.xcor()
    x+=100
    paddle.setx(x)

win.listen()
win.onkeypress(goLeft,"Left")
win.onkeypress(goRight,"Right")

while True:
    win.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*= -1
    elif ball.ycor()<-290:
        score-=1
        pen.clear()
        pen.write("score:{}".format(score),align="center",font=("Arial",24,"normal"))
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1

    if(ball.xcor() > paddle.xcor() -90) and \
      (ball.xcor() < paddle.xcor() +90) and \
       ball.ycor() < -230:
        ball.sety(-220)
        ball.dy*=-1
        score+=1
        pen.clear()
        pen.write("score:{}".format(score),align="center",font=("Arial",24,"normal"))
        
    
      



    
        
          
