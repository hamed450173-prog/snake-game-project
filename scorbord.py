from turtle import Turtle




class  the_caunt(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_score_bord()


    def update_score_bord(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",18,"normal"))



    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score_bord()


    def game_over(self):
        self.screen.bgcolor("dark red")
        self.goto(0,0)
        self.write(f"game over \n final Scoer: {self.score}",align="center",font=("Arial",25,"normal"))