from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(3.0, 1.0, 1)
        self.penup()
       
        
    def move_up(self):
        newy=self.ycor()+20
        self.goto(self.xcor(),newy)
        
            
    def move_down(self):
        
        newy=self.ycor()-20
        self.goto(self.xcor(),newy)
        




