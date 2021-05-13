import Player as p
import Dice as d

import time

BORDER = "=========================================="
DIVIDER = "------------------------------------------"

def how_to_play():
    print("There are only 4 rules I can tell you:\n"
          "1) The name of the game is 'Petals around the Rose'.\n"
          "2) The name of the game is important.\n"
          "3) Five dice will be rolled, and the computer will calculate a result.\n"
          "4) The result will always be an even number or 0."
        )
    time.sleep(3)
    
    print(DIVIDER)
    
    print("You can input your guess when prompted.\n"
          "If you'd like to stop playing, enter your guess as '-1'."
        )
    time.sleep(3)

    print(DIVIDER)

    print ("Beginning play in ~2 seconds...")
    
    time.sleep(2.5)

def game():
    player = p.Player()
    guess = 0
    while guess != -1:
        print(BORDER)
        if player.streak == 10:
            player.potentate = True

        dice = d.Dice()
        print(player)

        try:
            guess = int(input("Enter your guess as an integer: "))
        except:
            print("Please enter your guess as a valid integer!")
            guess = 3


        if guess == -1:
            break
        if guess != dice.result:
            print(f"Incorrect, the correct result is {dice.result}.")
            player.currentRoll += 1
            player.streak = 0
            time.sleep(2.5)
        if guess == dice.result:
            print(f"Correct! The result was {dice.result}.")
            player.currentRoll += 1
            player.correctGuess += 1
            player.streak += 1
            time.sleep(2.5)

def play():
    how_to_play()
    game()

