from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

b = Ball()
s = Screen()
s.listen()
sc = Score()

p1= Paddle()
p2 = Paddle()
p1.goto(-230, 0)
p2.goto(230, 0)

s.setup(width=500, height=500)
s.onkeypress(p1.move_up,"Up")
s.onkeypress(p1.move_down,"Down")
s.onkeypress(p2.move_up,"w")
s.onkeypress(p2.move_down,"s")
s.title("PONG")

game = True

x = 10
while game:
    time.sleep(0.1)
    b.move()
    if b.ycor() > 220 or b.ycor() < -220:
        b.bouncey()
    if b.distance(p2)<70 and b.xcor() > 200 or b.distance(p1)<70 and b.xcor() < -200:
        b.bouncex()
        b.speed(x)
        x-= 1
    
    if b.xcor() > 225 :
        b.reset_ball()
        sc.l_score+=1
        sc.update_score()
        
        
    if b.xcor() < -225:
        b.reset_ball()
        sc.r_score+=1
        sc.update_score()

        
        







s.exitonclick()