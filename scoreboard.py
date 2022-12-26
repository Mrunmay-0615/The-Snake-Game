from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")




class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            highscore = int(file.read())
        self.highscore = highscore
        self.hideturtle()
        self.goto(0, 275)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.highscore}", move=False, font=FONT, align=ALIGNMENT)

    def change_score(self, new_score):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.highscore = max(self.score, self.highscore)
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()