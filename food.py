from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-150, 150)
        random_y = random.randint(-150, 150)
        self.goto(random_x, random_y)
