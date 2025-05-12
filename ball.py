from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.movex=10
        self.movey=10
    
    def move(self):
        self.new_x = self.xcor() + self.movex
        self.new_y = self.ycor() + self.movey
        self.goto(self.new_x, self.new_y)
    
    def bouncey(self):
        self.movey*=-1
    
    def bouncex(self):
        self.movex *= -1
        
    def reset_ball(self):
        self.reset()
        self.penup()
        self.bouncex()