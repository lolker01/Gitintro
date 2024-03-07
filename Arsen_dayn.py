import turtle
from abc import ABC, abstractmethod

class Figures(ABC):
    def init(self, pen: turtle.Pen, x , y):
        self.pen = pen
        self.pen.up()
        self.pen.setheading(0)
        self.pen.goto(x, y)
        self.pen.down()
        self.pencolor = None
        self.set_color((0, 0, 0))
        
    def draw(self):
        pass
    
    def set_color(self, pencolor):
        self.pencolor = pencolor
        self.pen.pencolor(self.pencolor)
    
    @classmethod
    def same_color(cls, figure_1, figure_2):
        return figure_1.pencolor == figure_2.pencolor
    
class Square(Figures):
    def init(self, pen: turtle.Pen, x, y, size):
        super().init(pen, x, y)
        self.size = size
        
    def draw(self):
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.left(90)

class Circle(Figures):
    def init(self, pen: turtle.Pen, x, y, size):
        super().init(pen, x, y)
        self.size = size
        
    def draw(self):
        self.pen.circle(self.size)
      

turtle.colormode(255)

pen = turtle.Pen()

my_square_1 = Square(pen, -150, 0, 25)
my_square_1.draw()

my_square_2 = Square(pen, 150, 0, 25)
my_square_2.draw()

my_circle_1 = Circle(pen, 150, 150, 25)
my_circle_1.draw()
turtle.done

if (Figures.same_color(my_square_1, my_square_2)):
    print("Фігури однакових кольорів!.")
else:
    print("Фігури різних кольорів.")