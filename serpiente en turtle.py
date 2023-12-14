#MODULO
import turtle

#LIBRERIAS
import time
import random

#la velocidad del programa
posponer= 0.1

# Crear una nueva tortuga para el borde
borde = turtle.Turtle()

# Configurar la tortuga del borde
borde.penup()
borde.hideturtle()
borde.speed(0)
borde.color("white")

# Dibujar el borde
borde.goto(-285, -285)  # Ajusta las coordenadas según el tamaño de tu área de juego
borde.pendown()
for _ in range(4):
    borde.forward(575)  # Ajusta la longitud según el tamaño de tu área de juego
    borde.left(90)


#MARCADOR 
score= 0
high_score= 0

#para crear la ventana 
ventana= turtle.Screen()

#Para el titulo de la ventana 
ventana.title("Juego de la Serpiente")

#Para cambiar el color de fondo 
ventana.bgcolor("black")


#Tamaño de la ventana ancho x alto 
ventana.setup(width=690, height= 690)

#hace una mejora a las animaciones 
ventana.tracer(0)


#CABEZA
#cabeza de la serpiente (es solo para crear el objeto)
cabeza= turtle.Turtle()

#es para que este la forma en la pantalla
cabeza.speed(0)

#es para cambiar la forma 
cabeza.shape("square")

#color de la cabeza de la serpiente 
cabeza.color("orange")

#es para que no deje rastro
cabeza.penup()

#para dar una posicion en pantalla "es el centro"
cabeza.goto(0,0)

 #para dar direccion 
cabeza.direccion = "stop"

#COMIDA 
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente/segmentos(lista vacia)
segmentos=[]

#TEXTO
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()

#esconder la pluma que muestra el texto 
texto.hideturtle()
texto.goto(0,315)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Times New Roman", 24, "normal"))

#funciones 
def arriba():
    cabeza.direccion = "up"

def abajo():
    cabeza.direccion = "down"

def izquierda():
    cabeza.direccion = "left"

def derecha():
    cabeza.direccion = "right"


def mov():
    if cabeza.direccion == "up":
       #dame la coordenada y de mi cabeza 
        y= cabeza.ycor()
        #se va a ir moviendo 20 pixeles
        cabeza.sety(y + 20)

    if cabeza.direccion == "down":
        y= cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "left":
        x= cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direccion == "right":
        x= cabeza.xcor()
        cabeza.setx(x + 20)

#teclado
#este atenta a los eventos del teclado 
ventana.listen()

#si se presiona una tecla 
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

while True:
    ventana.update()

    #COLISIONES BORDES
    #si exede los limites pierde 
    if cabeza.xcor() > 285 or cabeza.xcor()< -285 or cabeza.ycor()  < -285 or cabeza.ycor() > 285:
        
        #da una pausa al juego 
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #ESCONDER LOS SEGMENTOS 
        for segmento in segmentos:
             segmento.goto(1000,1000)

        #LIMPIAR LISTA DE SEGMENTOS
        segmentos.clear()

        #RESETEAR MARCADOR
        score= 0
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score,high_score), align = "center", font = ("Times New Roman", 24, "normal"))

    #COLISIONES COMIDA
    if cabeza.distance(comida) < 20:

        #definimos un numero entero desde donde queremos que vaya tanto en x y Y
        x= random.randint(-285,285)
        y=random.randint(-285,285)
        #para actualizar la posicion de la comida 
        comida.goto(x,y)

        nuevo_segmento= turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        
        #es para agregar este segmento a la lista 
        segmentos.append(nuevo_segmento)

        #AUMENTAR MARCADOR
        score+= 10

        if score > high_score:
             high_score = score

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score,high_score), align = "center", font = ("Times New Roman", 24, "normal"))

        #MOVER EL CUERPO DE LA SERPIENTE 
        #obtener el total de los segmentos (len)
    totalSeg= len(segmentos)

    #hacemos que el ultimo elemento de siga al penultimo de los segmentos (el cero no se toma en cuenta y todos los demas numeros se le resta 1 )
    for index in range(totalSeg -1, 0, -1):
            x= segmentos[index - 1].xcor()
            y= segmentos[index - 1].ycor()
            #para que se mueva a las coordenadas
            segmentos[index].goto(x,y)

    if totalSeg > 0:
            x= cabeza.xcor()
            y= cabeza.ycor()
            #hacemos que el elemento se mueva donde esta la cabeza
            segmentos[0].goto(x,y)
    mov()
    
    #COLISIONES CUERPO
    for segmento in segmentos:
         if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direccion = "stop"


            #ESCONDER LOS SEGMENTOS 
            for segmento in segmentos:
                 segmento.goto(1000,1000)

            #LIMPIAR LOS ELEMENTOS DE LA LISTA
            segmentos.clear()


    #para que el programa no se ejecute tan rapido
    time.sleep(posponer)