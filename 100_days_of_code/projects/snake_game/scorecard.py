from turtle import Turtle

FONT = ("Arial", 20, "bold")
ALIGNMENT = "center"


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.score = 0
        self.shape("blank")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        # self.write((0, 250), False)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
