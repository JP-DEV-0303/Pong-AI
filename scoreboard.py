from turtle import Turtle
from playsound import playsound

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.a_score = 0
        self.r_score = 0

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.a_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def enemy_point(self):
        self.a_score += 1
        self.update()

    def player_point(self):
        self.r_score += 1
        self.update()

    def audio(self):
        if self.a_score == 11 or self.r_score == 11:
            playsound("PongAiAudio.wav")