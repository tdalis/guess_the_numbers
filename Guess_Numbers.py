# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# import the random library
import random

# Write the user_guess function
def user_guess():
    """
    Asks for the user to guess numbers and turns the strings to a list
    """
    return list(input("What is your guess?"))

# Write the code_generator function
def code_generator():
    """
    Generates three random numbers in a list
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

# Write the clues_generator function
def clues_generator(code, userGuess):
    """
    It takes the code generater by the machine and the user's guess then compares the numbers in a loop and creates a list of clues according to the matching parameters
    """
    if userGuess == code:
        return "Code Cracked!"

    clues = []

    # Compare guess to code
    for ind, num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run the Game
print("Welcome code breaker! Let's see if you can guess my three digit number!")

# Create a secret code to start the Game
secretCode = code_generator()
print("Code has been generated! Please guess a 3 digit number")
#print(secretCode)

# Empty clue report to start with
clueReport = []

# Keep asking until the user has gotten it right!
while clueReport != "Code Cracked!":

    # Ask for guess
    guess = user_guess()

    # Give the clues
    clueReport = clues_generator(guess, secretCode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
