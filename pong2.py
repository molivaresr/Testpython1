# Ventana inicio
import turtle

# Ventana inicio
win1 = turtle.Screen()
win1.title("Pong by Mau")
win1.bgcolor("black")
win1.bgpic("/Users/mauricioub/Documents/Github/Testpython1/pongimages/fondo2.png")
win1.setup(width= 800, height=600)
win1.tracer(0)

tle = turtle.Turtle()
tle.goto(0,0)
tle.color("white")
tle.hideturtle()
tle.penup()
tle.shapesize(stretch_len=200, stretch_wid=200)
tle.write("Bienvenido al PONG", align="center", font=("Courier", 50, "normal"))

msg = turtle.Turtle()
msg.goto(0,-250)
msg.color("white")
msg.hideturtle()
msg.penup()
msg.shapesize(stretch_len=200, stretch_wid=200)
msg.clear()   
msg.write("Presione START para comenzar" , align="center", font=("Courier", 30, "normal"))

def start_press():
    start = msg.xcor()
    start = start + 0.0001
    msg.setx(start)

win1.listen()
win1.onkeypress(start_press,"b")

while msg.xcor() == 0:
    win1.update()
else:
    win1.clear()
# Ventana 2
win2 = turtle.Screen()
win2.title("Pong by Mau")
win2.bgcolor("black")
win2.setup(width= 800, height=600)
win2.tracer(0)

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
# ball.speed(10)
ball.shape("circle")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

speedball = ball.speed(10)
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
    y = y + 20
    player1.sety(y)
def player1_down():
    y = player1.ycor()
    y = y - 20
    player1.sety(y)
def player2_up():
    y = player2.ycor()
    y = y + 20
    player2.sety(y)
def player2_down():
    y = player2.ycor()
    y = y - 20
    player2.sety(y)

# Teclado
win2.listen()
win2.onkeypress(player1_up,"w")
win2.onkeypress(player1_down,"s")
win2.onkeypress(player2_up,"Up")
win2.onkeypress(player2_down,"Down")

while True:
    win2.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Bordes eje y
    if ball.ycor() > 290:
        ball.dy = ball.dy * -1
    if ball.ycor() < -290:
        ball.dy = ball.dy * -1
# Bordes eje x
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        mark2 = mark2 + 1
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1    
        mark1 = mark1 + 1
    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < player2.ycor() + 50 
            and ball.ycor() > player2.ycor()-50)):
        ball.dx = ball.dx * -1
    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < player1.ycor()+50 
            and ball.ycor() > player1.ycor()-50)):
        ball.dx = ball.dx * -1  
    pen.clear() 
    pen.write("Jugador 1: " + str(mark1)+ "         "+"Jugador 2: " + str(mark2), align="center", font=("Courier", 24, "normal"))