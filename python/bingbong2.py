import turtle
# window generation
window=turtle.Screen()
turtle.title(" bing bong")
turtle.bgcolor("black")
turtle.setup(width=800, height=600)
turtle.tracer(0)

# madrab 1 generation
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350,0)
#madrab 1  motion
def madrab1_up():
   y=madrab1.ycor()
   y+=20
   madrab1.sety(y)
   if madrab1.ycor() > 250:
       madrab1.sety(250)

def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)
    if madrab1.ycor() <- 250:
        madrab1.sety(-250)
window.listen()
window.onkeypress(madrab1_up,"w")
window.onkeypress(madrab1_down,"s")
# madrab2 generation
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350,0)
#madrab 2 motion
def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)
    if madrab2.ycor() > 250:
        madrab2.sety(250)
def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)
    if madrab2.ycor() <- 250:
        madrab2.sety(-250)
window.listen()
window.onkeypress(madrab2_up,"Up")
window.onkeypress(madrab2_down,"Down")

#ball generation
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize()
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.2
ball.dy=.2

score=turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.color("white")
score.goto(0,250)
score.write("player1 = 0   player2 = 0 ", align="center", font=("Courier", 24, "normal"))
score1=0
score2=0











while True:
    turtle.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dy=-.2
        score2=score2+1
        score.clear()
        score.write("player1 = {}   player2 = {} ".format(score1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy=.2
        score1=score1+1
        score.clear()
        score.write("player1 = {}   player2 = {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))
    if(ball.xcor()>340 and ball.xcor()<350) and(ball.ycor()>madrab2.ycor()-40 and ball.ycor()<madrab2.ycor()+40) :
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor() <- 340 and ball.xcor() >- 350) and (
            ball.ycor() > madrab1.ycor() - 40 and ball.ycor() < madrab1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1