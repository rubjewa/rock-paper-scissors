import random

score = 0
choices = ['rock', 'paper', 'scissors']

computer_choice = ""
roundwin_choice = ""


print("\nWelkom bij Rock Paper Scissors, probeer de onverslaanbare computer te verslaan!!! \n")


def print_score():
    print("\nJe hebt " + str(score) + " punten :) \n")


#Check if score is still playable
while score >= 0 :
    user_choice = input('Choose your weapon: Rock/Paper/Scissors: ').lower()
    computer_choice = choices[random.randint(0, 2)]
    print("Computerkeuze: ", computer_choice.title())

    #Check if user choice is a valid choice
    if user_choice in choices:
        if user_choice == 'rock':
            roundwin_choice = 'paper'
        if user_choice == 'paper':
            roundwin_choice = 'scissors'
        if user_choice == 'scissors':
            roundwin_choice = 'rock'

    #If this is not the case the user will be prompted to choose again
    else:
        print("\nVerkeerde invoer, probeer opnieuw\n")

    #Check if computer made winning choice
    if len(roundwin_choice) != 0:
        if computer_choice == roundwin_choice :
            print("\nRonde Verloren")
            if score > 0:
                score -= 1
                roundwin_choice = ""
                print_score()
            else:
                print_score()
                print("------------------- Game over -------------------")
                break
        elif computer_choice == user_choice :
            print("\nGelijk spel :/ ")
            roundwin_choice = ""
            print_score()
        else:
            print("\nYou won!!")
            score += 1
            roundwin_choice = ""
            print_score()



