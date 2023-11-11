"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Stefan Kicak
email: stefan.kicak@gmail.com
discord: kico.mobil

"""

import random
import time

# global variables 
row = 47 * "-"
guesses = 0

# welcome and intro
print(f"Hi there!\n{row}\nI've generated a random 4-digit number for you.\nLet's play a bulls and cows game.\n{row}")

# 4 digit user input for starting the game
while True:
    user_input = input("Enter a 4-digit number with unique digits not starting with 0: ")
    if user_input.isdigit() and len(user_input) == 4 and len(set(user_input)) == 4:
        break
    else:
        print("\n\nInvalid input. Please enter a 4-digit number with unique digits not starting with 0.\n")
print("\n" + row)

# auto-generated 4-digit number. Not starting with zero and not repetitive digits
generated_number = int(''.join(map(str, random.sample(range(1, 10), 4))))

# print generated number for check during tests
# print(generated_number)

# make lists from generated number
generated_number_digits = list(map(int, str(generated_number)))

start_time = time.time()

while True:
    # print user input
    print(">>> " + user_input)

    # make list from user input
    user_input_number_digits = list(map(int, str(user_input)))

    # compare the two lists
    bulls = sum(x == y for x, y in zip(generated_number_digits, user_input_number_digits))
    cows = sum(min(generated_number_digits.count(digit), user_input_number_digits.count(digit)) for digit in set(generated_number_digits))

    # print results
    print(row)
    if bulls == 1:
        print(f"{bulls} bull")
    else:
        print(f"{bulls} bulls")

    if cows == 1:
        print(f"{cows} cow")
    else:
        print(f"{cows} cows")

    guesses += 1

    # check if all positions are correct
    if bulls == 4:
        print(row)
        end_time = time.time()
        elapsed_time = round(end_time - start_time)
        print(f"Congratulations! You guessed the correct number {generated_number} in {guesses} guesses and {elapsed_time} seconds.")
        break

    # get a new guess from the user
    while True:
        print(row)
        user_input = input("Try again: ")
        if user_input.isdigit() and len(user_input) == 4 and len(set(user_input)) == 4:
            break
        else:
            print(row)
            print("\n\nInvalid input. Please enter a 4-digit number with unique digits not starting with 0.\n")