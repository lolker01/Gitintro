import turtle

window = turtle.Screen()
window.bgcolor("Sky blue")

pen = turtle.Turtle()
pen.speed(7)

def draw_rectangle():
    pen.fillcolor("lightgrey")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(150)
        pen.left(90)
    pen.end_fill()

def draw_roof():
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.up()
    pen.goto(-20, 150)
    pen.down()
    pen.goto(220, 150)
    pen.goto(100, 300)
    pen.goto(-20, 150)
    pen.end_fill()

def draw_window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black")
    pen.fillcolor("yellow")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
  


draw_rectangle()

draw_roof()

draw_window(30, 100)
draw_window(130, 100)
turtle.done()