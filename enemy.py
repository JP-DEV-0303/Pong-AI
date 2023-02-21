from paddle import Paddle


class EnemyAI(Paddle):
    def __init__(self, position, hardness):
        super().__init__(position=position)
        self.move_speed = 10
        self.color("red")
        self.goto(position)
        self.hardness = hardness
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
        if self.hardness == "Easy":                
            new_y = self.ycor()-1.5
            self.goto(self.xcor(), new_y)

        elif self.hardness == "Medium":                
            new_y = self.ycor()-1
            self.goto(self.xcor(), new_y)

        elif self.hardness == "Hard":                
            new_y = self.ycor()-0.5
            self.goto(self.xcor(), new_y)

        else:
            pass

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
        if self.hardness == "Easy":                
            new_y = self.ycor()+1.5
            self.goto(self.xcor(), new_y)

        elif self.hardness == "Medium":                
            new_y = self.ycor()+1
            self.goto(self.xcor(), new_y)

        elif self.hardness == "Hard":                
            new_y = self.ycor()+0.5
            self.goto(self.xcor(), new_y)

        else:
            pass)
