from turtle import Turtle





class Snake():
    def __init__(self):
        self.postion=((0,0),(20,0),(40,0))
        self.colors=("white")
        self.turtles=[]
        self.creet_snake()
        self.head=self.turtles[-1]





    def creet_snake(self):
        for i in range(len(self.postion)):
            new_turtles = Turtle()
            new_turtles.shape("square")
            new_turtles.color("white")
            new_turtles.penup()
            new_turtles.goto(self.postion[i])
            self.turtles.append(new_turtles)

    def the_taal(self):
        new_tall = Turtle("square")
        new_tall.color("white")
        new_tall.penup()
        new_tall.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_tall)

    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())

        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)






