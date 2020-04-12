import turtle

# ajustar las posiciones iniciales para
# que la hormiga no salga desfasada con 
# respecto a la grilla.

def ajuste(x0,y0):
    x0 = (x0//5)*5
    y0 = (y0//5)*5
    if x0%2 == 0:
        x0 = x0 +5
    if y0%2 == 0:
        y0 = y0 +5
    print(x0)
    print(y0)
    ant.setposition(x0,y0)

# inicializacion de hormiga y screen
ant = turtle.Turtle()
turtle.setup(1280,720)

# inputs de numero de cuadriculas y numero de movimientos
numcuad = int(turtle.textinput("SETTINGS","Digite numero de cuadriculas"))
nummov = int(turtle.textinput("SETTINGS","Digite numero de movimientos"))

# limites superior e inferior 
asg = (numcuad//2)*10  
asgg = (numcuad//2)*(-10)

# input de posicion inicial x_0 
x0 = -10101010
while x0>=asg or x0<=asgg:
    x0 = int(turtle.textinput("SETTINGS","Digite coordenada x0"))

# input de posicion inicial y_0
y0 = -1010101001
while y0>=asg or y0<=asgg:
    y0 = int(turtle.textinput("SETTINGS","Digite coordenada y0"))

# creacion de la cuadricula
def grid(numcuad):
    step = 10
    for i in range(numcuad):
        for k in range(numcuad):
            for j in range(4):
                ant.forward(10)
                ant.right(90)
            ant.forward(step)
        ant.right(90)
        ant.forward(10)
        ant.right(90)
        ant.forward(10*numcuad)
        ant.right(180)

# actualizacion el color del espacio donde esta la hormiga
def update_maps(graph, turtle, color):
    graph[turtle_pos(turtle)] = color
    return None

# funcion para saber la posicion actual de la hormiga
def turtle_pos(turtle):
    return (round(turtle.xcor()), round(turtle.ycor()))

# definicion de las condiciones iniciales del problema
def langton_move(turtle, pos, maps, step):
    if pos not in maps or maps[pos] == "white":
        turtle.fillcolor("black")
        turtle.stamp()
        update_maps(maps, turtle, "black")
        turtle.right(90)
        turtle.forward(step)
        pos = turtle_pos(turtle)
    elif maps[pos] == "black":
        turtle.fillcolor("white")
        update_maps(maps, turtle, "white")
        turtle.stamp()
        turtle.left(90)
        turtle.forward(step)
        pos = turtle_pos(turtle)
    return pos

# funcion para no pasarse de los movimientos
# pre-establecidos y que la hormiga no se 
# salga de la grilla.
def move():

    maps = {}
    step = 10
    ant.penup()
    ant.speed(-1)
    ant.right(180)

    pos = turtle_pos(ant)
    moves = 0
    xcor = ant.xcor()
    ycor = ant.ycor()
    while moves!=nummov and xcor>=asgg and xcor<=asg and ycor>=asgg and ycor<=asg:
        pos = langton_move(ant, pos, maps, step)
        moves += 1
        xcor = ant.xcor()
        ycor = ant.ycor()
        print ("Movements:", moves)
        print(pos)


# main
ant.hideturtle()
ant.penup()
ant.goto((numcuad//2)*10,(numcuad//2)*10)
print(ant.pos())
print(ant.xcor())
print(ant.ycor())
ant.right(90)
ant.pendown()
ant.speed('fastest')
turtle.tracer(numcuad,0)
grid(numcuad)
ant.isvisible()
ant.penup()
ant.goto(x0,y0)
print(ant.pos())
ant.pendown()
ajuste(x0,y0)
ant.color('black')
ant.shape('square')
ant.shapesize(0.5)
move()
ant.color('red')
ant.shape('arrow')
ant.pendown()
ant.forward(10)
ant.stamp()
input()


