from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-50, 180)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(50, 180)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
        