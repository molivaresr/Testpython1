import turtle
import time
import random
slow = 0.1

# Ventana Secundaria
win2 = turtle.Screen()
win2.title("Snake by Mau")
win2.bgcolor("black")
win2.setup(width= 800, height= 800)
win2.tracer(0)

# Serpiente
snk = turtle.Turtle()
snk.speed(20)
snk.shape("square")
snk.shapesize(stretch_len=1, stretch_wid=1)
snk.color("white")
snk.penup()
snk.goto(0,0)
snk.direction = "stop"

# Cuerpo
tail = []

# Food
food = turtle.Turtle()
food.speed()
food.shape("circle")
food.color("red")
food.shapesize(stretch_len=1, stretch_wid=1)
food.penup()
food_x = random.randint(-360,360)
food_y = random.randint(-360,360)
food.goto(food_x,food_y)

# food_life.speed()
# food_life.shape("circle")
# food_life.color("green")
# food_life.shapesize(stretch_len=1, stretch_wid=1)
# food_life.penup()
# foodlife_x = random.randint(-360,360)
# foodlife_y = random.randint(-360,360)
# food_life.goto(foodlife_x,foodlife_y)
# Marcador 
score = 0
highscore= 0
life = 3

msg = turtle.Turtle()
msg.goto(0,375)
msg.color("white")
msg.hideturtle()
msg.penup()
msg.shapesize(stretch_len=200, stretch_wid=200)
msg.clear()   

gover = turtle.Turtle()
gover.goto(0,50)
gover.color("white")
gover.hideturtle()
gover.penup()
gover.shapesize(stretch_len=200, stretch_wid=200)
gover.clear() 

line_up = turtle.Turtle()
line_up.speed(0)
line_up.shape("square")
line_up.shapesize(stretch_len=800, stretch_wid=0.05)
line_up.color("white")
line_up.penup()
line_up.goto(0,380)

line_down = turtle.Turtle()
line_down.speed(0)
line_down.shape("square")
line_down.shapesize(stretch_len=800, stretch_wid=0.05)
line_down.color("white")
line_down.penup()
line_down.goto(0,-380)

line_left = turtle.Turtle()
line_left.speed(0)
line_left.shape("square")
line_left.shapesize(stretch_len=0.05, stretch_wid=800)
line_left.color("white")
line_left.penup()
line_left.goto(-380,0)

line_right = turtle.Turtle()
line_right.speed(0)
line_right.shape("square")
line_right.shapesize(stretch_len=0.05, stretch_wid=800)
line_right.color("white")
line_right.penup()
line_right.goto(380,0)
  
# Funciones
def up():
    snk.direction = "up"
def down():
    snk.direction = "down"
def left():
    snk.direction = "left"
def right():
    snk.direction = "right"

def mov_on():
    if snk.direction == "up":
        snk_y = snk.ycor()
        snk.sety(snk_y + 20)
    if snk.direction == "down":
        snk_y = snk.ycor()
        snk.sety(snk_y - 20)
    if snk.direction == "left":
        snk_x = snk.xcor()
        snk.setx(snk_x - 20)
    if snk.direction == "right":
        snk_x = snk.xcor()
        snk.setx(snk_x + 20)
def mov_off():
    snk.direction = "stop"

# Teclado
win2.listen()
win2.onkeypress(up,"Up")
win2.onkeypress(down,"Down")
win2.onkeypress(left,"Left")
win2.onkeypress(right,"Right")

while True:
    win2.update()
    # Colisión
    if snk.distance(food) < 15:
        food_x = random.randint(-360,360)
        food_y = random.randint(-360,360)
        food.goto(food_x,food_y)
        score = score + 1
        if score > highscore:
            highscore = score
            
        # Cola
        snk_tail = turtle.Turtle()
        snk_tail.speed(20)
        snk_tail.shape("square")
        snk_tail.shapesize(stretch_len=1, stretch_wid=1)
        snk_tail.color("grey")
        snk_tail.penup()
        tail.append(snk_tail)

    # Mover la cola 
    tot_tail = len(tail)
    for index in range(tot_tail -1, 0, -1):
        tail_x= tail[index -1].xcor()
        tail_y = tail[index -1].ycor()
        tail[index].goto(tail_x,tail_y)
    if tot_tail > 0:
        tail_x = snk.xcor()
        tail_y = snk.ycor()
        tail[0].goto(tail_x, tail_y)
    # Colisión paredes
    if snk.xcor() > 360 or snk.xcor() < -360 or snk.ycor() > 360 or snk.ycor() < -360:
        time.sleep(1)
        snk.goto(0,0) 
        snk.direction="stop"
        score = 0
        life = life - 1
        if score > highscore:
            highscore = score
        # Desapareciendo la cola
        for tail_2 in tail:
            tail_2.goto(1000,1000)
            tail = []
    mov_on()
   #  Colisión Snake
    for tail_2 in tail:
        if tail_2.distance(snk) < 5:
            time.sleep(1)
            snk.goto(0,0)
            snk.direction="stop"
            for tail_2 in tail:
                tail_2.goto(1000,1000)
                tail =[]
            life = life -1    

    msg.clear()
    msg.write("Puntos: {} Vidas: {} Record: {} ".format(score,life,highscore) , align="center", font=("Courier", 24, "normal"))
    
    if life == 0:
        gover.write("G A M E  O V E R", align="center", font=("Courier", 40, "normal"))
        snk.color("white")
        mov_off()
    
    time.sleep(slow)