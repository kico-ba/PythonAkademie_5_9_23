"""
projekt_2.py: druhý (opraveny) projekt do Engeto Online Python Akademie
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
player_name = input("Put your name here: ")
print(f"Hi {player_name}!\n{row}\nI've generated a random 4-digit number for you.\nLet's play a bulls and cows game.\n{row}")


def digit_user_input():
    while True:
        user_input = input("Enter a 4-digit number with unique digits not starting with 0: ")
        if user_input.isdigit() and len(user_input) == 4 and user_input[0] != '0' and len(set(user_input)) == 4:
            return user_input
        else:
            print("\nInvalid input. Please enter a 4-digit number with unique digits not starting with 0.\n")
validated_input = digit_user_input()

def write_score():
    with open("score.txt", mode="a") as txt_file:
            txt_file.write(f"{player_name} - {guesses} guesses and {elapsed_time} sec\n")

# auto-generated 4-digit number. Not starting with zero and not repetitive digits
generated_number = str(random.randint(1000, 9999))
# print(generated_number) 

# convert to list
generated_number_digits = list(map(int, generated_number))

start_time = time.time()

while True:
    # print user input
    print(f">>> {validated_input}")

    # make list from user input
    user_input_number_digits = list(map(int, validated_input))

    # compare the two lists
    bulls = sum(x == y for x, y in zip(generated_number_digits, user_input_number_digits))
    cows = len(set(generated_number_digits) & set(user_input_number_digits))-bulls

    # print results
    print(row)
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}")
    print(f"{cows} {'cow' if cows == 1 else 'cows'}")

    guesses += 1

    # check if all positions are correct
    if bulls == 4:
        print(row)
        end_time = time.time()
        elapsed_time = round(end_time - start_time)
        print(f"Congratulations! You guessed the correct number {generated_number} in {guesses} guesses and {elapsed_time} seconds.")
        write_score()
        break
# get a new guess from the user
    print(row)
    validated_input = digit_user_input()
