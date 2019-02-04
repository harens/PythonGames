# Please note that the comments here were meant to act as questions to help the user understand how the code functions

from random import randint, choice  # What do you make choices on?
from time import (
    sleep,
)  # Do you do a lot while sleeping? How does this module make the computer more realistic?
from string import (
    ascii_lowercase,
)  # Just a string of lowercase letters, but why is it needed?
import copy  # What are the ways of copying a list?

co_ordinates = [
    " ",
    "A",
    "",
    "B",
    "",
    "C",
    "",
    "D",
    "",
    "E",
    "",
    "F",
    "",
    "G",
    "",
    "H",
    "",
    "I",
]
# How does an English Dictionary work?
all_ships = {
    "Destroyer": 2,
    "Submarine": 3,
    "Cruiser": 3,
    "Battleship": 4,
    "Aircraft Carrier": 5,
}
all_directions = ["up", "down", "left", "right"]

# Can you have a list in a list? When would you want this?
user_board = []
for y_direction in range(0, 8):
    final_list = []
    for x_direction in range(0, 9):
        final_list.append("🌊")
    user_board.append(final_list)

computer_board = copy.deepcopy(user_board)
guess_board = copy.deepcopy(user_board)


def boat_placement(direction, length, board, position):
    # Do you always want the program to terminate when there's an error?
    try:
        for ship_place in range(0, length):
            if direction == "up" or direction == "u":
                if (
                    board[position[1] - ship_place][position[0]] == "🚢"
                    or (position[1] - ship_place) < 0
                ):
                    return False
                # How do you find the position of an item in a list? How would you do this for a list in a list?
                board[position[1] - ship_place][position[0]] = "🚢"
            elif direction == "down" or direction == "d":
                if board[position[1] + ship_place][position[0]] == "🚢":
                    return False
                board[position[1] + ship_place][position[0]] = "🚢"
            elif direction == "left" or direction == "l":
                if (
                    board[position[1]][position[0] - ship_place] == "🚢"
                    or (position[0] - ship_place) < 0
                ):
                    return False
                board[position[1]][position[0] - ship_place] = "🚢"
            elif direction == "right" or direction == "r":
                if (
                    board[position[1]][position[0] + ship_place] == "🚢"
                    or (position[0] + ship_place) > 8
                ):
                    return False
                board[position[1]][position[0] + ship_place] = "🚢"
            else:
                return False
        return board
    # What does an index in a book do?
    except IndexError:
        return False


def print_board(board):
    print("")
    for board_output in range(0, 8):
        # Why is the number 7 used here? Think about the direction of the axes.
        y_axis = str(7 - board_output)
        # Do you need a space between the apostrophes? Try typing a letter inside and see what happens...
        print(y_axis, " ".join(board[board_output]))
    print(" ".join(co_ordinates))
    print("")


for ship in all_ships:

    # Why is an original copy of the board needed?
    original_board = copy.deepcopy(user_board)

    print_board(user_board)

    while True:
        # `.lower()` has been used a lot in this program, what does it do? Think about what you can do to letters
        user_placement = input(
            "Where would you like to place your {0} (length: {1})? ".format(
                ship, all_ships[ship]
            )
        ).lower()  # Notice the curly brackets with a number...what do they show when you run them?
        ship_position = []
        for char in user_placement:
            # What does the word `alpha` look like?
            if char.isalpha():
                ship_position.insert(0, ascii_lowercase.index(char))
            else:
                ship_position.insert(1, int(char))

        # Why is the number 7 here again! Also, why can you NOT do `ship_position[1] -= 7` instead?
        ship_position[1] = 7 - ship_position[1]

        user_direction = input(
            "Which direction would you like it to face? [up/down/left/right] "
        ).lower()
        new_board = boat_placement(
            user_direction, all_ships[ship], user_board, ship_position
        )
        if new_board is not False:
            user_board = copy.deepcopy(new_board)
            # If you break away from something, what are you doing?
            break
        else:
            # What does \n do? Try testing it out with print statements
            print("Invalid Option\n")
            user_board = copy.deepcopy(original_board)

print("All boats placed!\n")
print("Computer is thinking...")


for computer_ship in all_ships:

    original_computer = copy.deepcopy(computer_board)

    # Why are only random numbers generated, when the axes has letters?
    computer_position = [randint(0, 8), randint(0, 7)]
    while True:
        while computer_board[computer_position[1]][computer_position[0]] == "🚢":
            computer_position = [randint(0, 8), randint(0, 7)]
        computer_direction = choice(all_directions)
        new_computer = boat_placement(
            computer_direction,
            all_ships[computer_ship],
            computer_board,
            computer_position,
        )
        if new_computer is not False:
            computer_board = copy.deepcopy(new_computer)
            break
        else:
            computer_board = copy.deepcopy(original_computer)

# Look at the very bottom line for a hint as to what this does ↴
final_output = copy.deepcopy(computer_board)

print("Computer is ready!")
sleep(1)

# Think of any() like an `or` statement. Only one of the items has to be a boat.
while any("🚢" in user_list for user_list in user_board) and any(
    "🚢" in computer_list for computer_list in computer_board
):
    print("")
    print("This is your board:\n")
    print_board(user_board)
    print("This is your guessing board:\n")
    print_board(guess_board)

    # There are three main types of boards that have now been used
    # Hopefully this will help you keep track!

    # user_board => This is where you place your ships
    # computer_board => This is where the computer places their ships
    # guess_board => This shows you where you've aimed

    aim_position = []
    user_aim = input("Where would you like to aim? ").lower()

    for letter in user_aim:
        if letter.isalpha():
            aim_position.insert(0, ascii_lowercase.index(letter))
        else:
            aim_position.insert(1, int(letter))

    aim_position[1] = 7 - aim_position[1]

    if computer_board[aim_position[1]][aim_position[0]] == "🚢":
        print("Enemy Boat Hit!")
        guess_board[aim_position[1]][aim_position[0]] = "✅"
        computer_board[aim_position[1]][aim_position[0]] = "🔥"
    else:
        print("Missed")
        guess_board[aim_position[1]][aim_position[0]] = "❌️"

    sleep(1)
    print("Computer is aiming...")
    sleep(1.5)

    while True:
        computer_aim = [randint(0, 8), randint(0, 7)]
        if user_board[computer_aim[1]][computer_aim[0]] == "🚢":
            print("Friendly Boat Hit!")
            user_board[computer_aim[1]][computer_aim[0]] = "🔥"
            break
        # Why is this elif statement here?
        elif (
            user_board[computer_aim[1]][computer_aim[0]] == "❌"
            or user_board[computer_aim[1]][computer_aim[0]] == "🔥"
        ):
            continue  # If you continue with something, what are you doing?
        else:
            print("The Enemy Missed!")
            user_board[computer_aim[1]][computer_aim[0]] = "❌"
            break

    sleep(1)

print("")

if any("🚢" in user_list for user_list in user_board):
    print("You Win!\n")
else:
    print("You Lost\n")

print("This was the enemy's board:")
print_board(final_output)


# EXTENSIONS:
# What happens if someone aims in the same place twice?
# How can you improve the computer's aiming?
# Can you show when a ship has sunk?
