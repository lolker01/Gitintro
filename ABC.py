import turtle
from abc import ABC, abstractmethod

class Figures():
    def __init__(self, pen: turtle.Pen, x , y):
        self.pen = pen
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()
        self.pencolor = None
        self.set_color((0, 0, 0))
    @abstractmethod
    def draw(self):
        pass
    def set_color(self, pencolor):
        self.pencolor = pencolor
        self.pen.pencolor(pen.pencolor)

pen = turtle.Pen()
my_figure = Figures(pen, 10, 20)
my_figure.draw()
    