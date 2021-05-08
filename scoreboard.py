from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.level = 1
        self.color("black")

    def write_level(self):
        self.clear()
        self.write(f"level : {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(-80, 0)
        self.write(f"Game Over", move=False, align="left", font=FONT)


