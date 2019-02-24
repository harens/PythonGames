guess_word = "hello"  # ENTER WORD HERE
correct_chars = []  # User's correct characters
print_output = []  # Shows current status
number_lives = 5  # ENTER LIVES HERE

for counter in range(0, len(guess_word)):
    print_output.append("_")

while number_lives > 0:
    print("")
    print(" ".join(print_output))
    print("Lives:", "❤" * number_lives)
    user_letter = input("Enter letter: ")
    if user_letter in guess_word:  # If input is correct
        print("Correct!")
        correct_chars.append(user_letter)
        print_output = []
        for char in guess_word:
            if char in correct_chars:  # Displays correct character if already inputted
                print_output.append(char)
            else:
                print_output.append(
                    "_"
                )  # Displays '-' if character has not been inputted
        if "".join(print_output) == guess_word:
            print("")
            print("You Win!")
            print("The word was:", guess_word)
            break
    else:
        print("Incorrect")
        number_lives -= 1

if number_lives == 0:
    print("")
    print("You lost")
    print("The word was:", guess_word)
