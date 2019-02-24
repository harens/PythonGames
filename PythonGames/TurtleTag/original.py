from turtle import Screen, Turtle
from random import randint
from tkinter import messagebox, Tk

window = Tk()
window.withdraw()


def chase_move(x_cor, y_cor):  # _cor is where the mouse wants to go
    random_x = randint(-200, 200)  # Random positions of the turtle
    random_y = randint(-200, 200)
    # While the user_arrow is close to where the Chased-Turtle wants to go
    while user_arrow.distance(random_x, random_y) <= 100:
        random_x = randint(-200, 200)
        random_y = randint(-200, 200)
    user_arrow.clear()  # Removes their drawn lines
    turtle.clear()

    turtle.goto(random_x, random_y)
    user_arrow.goto(x_cor, y_cor)

    if turtle.distance(user_arrow) <= 65:  # This checks if the arrow hits the turtle
        user_arrow.color("red")
        turtle.color("red")
        global tk
        messagebox.showinfo(
            "Turtle Tag!", "You caught the Turtle!\nYou Win!"
        )  # \n adds a new line
        screen.bye()
        return


screen = Screen()  # Sets up Screen size and grid
screen.bgcolor("lightblue")
screen.setup(600, 600)
screen.screensize(500, 500)
screen.title("Turtle Tag!")

user_arrow = Turtle()  # Arrow shape instead of a Turtle shape
turtle = Turtle("turtle")

turtle.color("darkgreen")
user_arrow.color("blue")

turtle.shapesize(7)
turtle.pensize(3)

# Moves the Chased-Turtle so it and the arrow don't start in the same position
turtle.pu()  # Pen Up shorthand
turtle.left(90)
turtle.forward(100)
turtle.pd()

screen.onclick(chase_move)  # Runs the function when the screen is clicked

screen.mainloop()
window.mainloop()
