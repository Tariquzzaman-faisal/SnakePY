from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

khana = Food()
tim = Snake()
point = Scoreboard()

#Initializeing the screen
screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")

game_on = True

#Main game loop
while(game_on):
    screen.update()
    #Game speed
    time.sleep(0.1)
    tim.move()

    #Food eating condition
    if(tim.head.distance(khana) < 15):
        khana.respawn()
        point.increase_score()
        tim.extend()
    #Wall collision
    if tim.head.xcor() > 280 or tim.head.ycor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() < -280 :
        point.reset()
        tim.reset()
    #Tail collision
    for segment in tim.segments:
        if segment == tim.head:
            pass
        elif tim.head.distance(segment) < 10:
            point.reset()
            tim.reset()
screen.exitonclick()
