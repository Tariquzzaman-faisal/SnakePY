from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        ranX = random.randint(-200, 200)
        ranY = random.randint(-200, 200)
        self.goto(ranX, ranY)
    
