from time import sleep
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scorbord import the_caunt
import time


window=Screen()
window.setup(600,600)
window.title("عم المجال✌")
window.bgcolor("black")
window.tracer(0)


abdulhameed=Snake()
the_apper=Food()
score=the_caunt()








my_game=True
while my_game:
    window.update()
    sleep(0.1)
    abdulhameed.move()
    window.listen()
    window.onkey(abdulhameed.up, "Up")
    window.onkey(abdulhameed.down, "Down")
    window.onkey(abdulhameed.right, "Right")
    window.onkey(abdulhameed.left, "Left")

    if abdulhameed.head.distance(the_apper) <15:
        the_apper.appear()
        abdulhameed.the_taal()
        score.increase_score()


    if abdulhameed.head.xcor()>280or abdulhameed.head.xcor()<-280 or abdulhameed.head.ycor()>280or abdulhameed.head.ycor()<-280:
        my_game=False
        score.game_over()


    for segment in abdulhameed.turtles[:-1]:
        if abdulhameed.head.distance(segment) < 10:
            my_game=False
            score.game_over()



window.exitonclick()
