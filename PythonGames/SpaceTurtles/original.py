from turtle import Screen, Turtle
from random import randint, choice
from tkinter import messagebox, Tk

window = Tk()  # Creates and hides final output window
window.withdraw()


def end_game():  # Determines if game is over
    for item in rocket_list:
        if (
            user_turtle.distance(item) <= 40
        ):  # Check's distance from turtle to each rocket
            screen.bye()  # Closes the screen
            messagebox.showinfo("Space Turtles!", "You got hit!")
            window.mainloop()  # Acts as end of program


def move_rocket():  # Moves rockets to positions
    for rocket in rocket_list:
        rocket.clear()  # Removes drawings
        rocket.pd()
        rocket.speed(randint(1, 10))
        rocket.fd(300)  # How far down to go
        end_game()  # Checks if turtle has been hit
        rocket.goto(randint(-290, 290), 290)  # Moves rocket to random position
    screen.ontimer(move_rocket, 300)  # Runs function every 300 milliseconds


def create_rocket(rocket):
    rocket.seth(270)  # Changes direction to South
    rocket.color(
        choice(["violet", "yellow", "lightblue", "darkgreen", "pink", "brown", "beige"])
    )
    rocket.goto(randint(-290, 290), 290)  # Moves rocket to random position
    rocket.turtlesize(3)


screen = Screen()  # Sets up Screen size and grid
screen.bgcolor("darkblue")
screen.setup(600, 600)
screen.title("Space Turtles!")

rocket_1 = Turtle()  # Initialises the rockets
create_rocket(rocket_1)

rocket_2 = Turtle()
create_rocket(rocket_2)

rocket_3 = Turtle()
create_rocket(rocket_3)

rocket_list = [rocket_1, rocket_2, rocket_3]

user_turtle = Turtle("turtle")  # Creates the user's character
user_turtle.pu()
user_turtle.color("green")
user_turtle.turtlesize(3)


def rocket_left():  # Functions that control direction
    user_turtle.bk(5)


def rocket_right():
    user_turtle.fd(5)


screen.onkey(rocket_left, "a")  # Runs different functions depending on the key
screen.onkey(rocket_right, "d")

screen.listen()  # Listens fo key presses

move_rocket()  # Moves the rockets for the first time
