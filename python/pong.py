import turtle


tela = turtle.Screen()
tela.title("Pong por: Everton B.S")
tela.bgcolor("black")
tela.setup(width= 800 , height= 600)
tela.tracer(0)


#Raquete A
raquete_a = turtle.Turtle()
raquete_a.shape("square")
raquete_a.speed(0)
raquete_a.color("white")
raquete_a.shapesize(stretch_wid= 5, stretch_len= 1)
raquete_a.penup()
raquete_a.goto(-350, 0)


#Raquete B
raquete_b = turtle.Turtle()
raquete_b.shape("square")
raquete_b.speed(0)
raquete_b.color("white")
raquete_b.shapesize(stretch_wid= 5, stretch_len= 1)
raquete_b.penup()
raquete_b.goto(350, 0)


#Bola
bola = turtle.Turtle()
bola.shape("circle")
bola.speed(0)
bola.color("red")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.8
bola.dy = -0.8

#Funções subir e descer raquetes...
def raquete_a_up():
    y = raquete_a.ycor()
    y += 20
    raquete_a.sety(y)

def raquete_a_down():
    y = raquete_a.ycor()
    y -= 20
    raquete_a.sety(y)

def raquete_b_up():
    y = raquete_b.ycor()
    y += 20
    raquete_b.sety(y)

def raquete_b_down():
    y = raquete_b.ycor()
    y -= 20
    raquete_b.sety(y)

#Leitura do teclado
tela.listen()
tela.onkeypress(raquete_a_up, "w")
tela.onkeypress(raquete_a_down, "s")
tela.onkeypress(raquete_b_up, "Up")
tela.onkeypress(raquete_b_down, "Down")

##Loop do Jogo princpal

while True:
    tela.update()

    #Movimento da Bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #Bater na borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1

    #Colisão da bola com as raquetes
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 50 and bola.ycor() > raquete_b.ycor() -50):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 50 and bola.ycor() > raquete_a.ycor() -50):
        bola.setx(-340)
        bola.dx *= -1
    


