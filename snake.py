from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

EAT = 3

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        b = Turtle("square")
        b.color("white")
        b.penup()
        b.goto(position)
        self.body.append(b)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.body[-1].position())

    def move(self):
        for a in range(len(self.body) - 1, 0, -1):
            new_x = self.body[a - 1].xcor()
            new_y = self.body[a - 1].ycor()
            self.body[a].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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