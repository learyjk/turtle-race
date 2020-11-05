from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win? (color):")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start_y = -100

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.speed("fastest")
    t.penup()
    t.goto(x=-230, y=start_y)
    start_y += 40
    turtles.append(t)

no_winner = True
while no_winner:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            print(f"The {winner} turtle is the winner!")
            if winner == user_bet:
                print("You win!")
            else:
                print("You lose!")
            no_winner = False
            break
        turtle.forward(randint(0, 20))

screen.exitonclick()