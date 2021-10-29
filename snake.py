from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVING_DISTANCE = 20
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.createSegments()
        self.head = self.segments[0]

    def createSegments(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        newSeg = Turtle("square")
        newSeg.color("white")
        newSeg.penup()
        newSeg.goto(position)
        self.segments.append(newSeg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum-1].xcor()
            newY = self.segments[segNum-1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.segments[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createSegments()
        self.head = self.segments[0]

