from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.board()

    def board(self):
        self.write(f"Score: {self.score}", move = False, align = "center", font = ('Courier', 18, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Courier', 20, 'normal'))

    def sum(self):
        self.score += 1
        self.clear()
        self.board()