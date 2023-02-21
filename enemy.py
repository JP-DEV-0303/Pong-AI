from paddle import Paddle


class EnemyAI(Paddle):
    def __init__(self, position):
        super().__init__(position=position)
        self.move_speed = 20
        self.color("red")
        self.goto(position)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)