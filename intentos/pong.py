import turtle

# Ventana
wn = turtle.Screen()
wn.title("Pong by Mau")
wn.bgcolor("black")
wn.setup(width= 800, height=600)
wn.tracer(0)
# Marcador
mark1 = 0
mark2 = 0
# Player 1
player1 = turtle.Turtle()
player1.speed(1)
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("white")
player1.penup()
player1.goto(-350,0)

# Player 2
player2 = turtle.Turtle()
player2.speed(1)
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("white")
player2.penup()
player2.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

# Linea
line = turtle.Turtle()
line.color("white")
line.goto(0,0)
line.shapesize(stretch_len=0.05, stretch_wid=400)
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

# Funciones
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)
def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)
def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)
def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

# Teclado
wn.listen()
wn.onkeypress(player1_up,"w")
wn.onkeypress(player1_down,"s")
wn.onkeypress(player2_up,"Up")
wn.onkeypress(player2_down,"Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Bordes eje y
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1
# Bordes eje x
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        mark2 += 1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1    
        mark1 += 1
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < player2.ycor() + 50 
            and ball.ycor() > player2.ycor()-50)):
        ball.dx *= -1
    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < player1.ycor()+50 
            and ball.ycor() > player1.ycor()-50)):
        ball.dx *= -1
    pen.clear() 
    pen.write("Jugador 1: " + str(mark1)+ "         "+"Jugador 2: " + str(mark2), align="center", font=("Courier", 24, "normal"))