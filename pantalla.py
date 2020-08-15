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

