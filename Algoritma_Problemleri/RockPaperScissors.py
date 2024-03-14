# from random import randint
from random import choice

t = ["Rock","Paper","Scissors"]
# computer = t[randint(0,2)]
# computer  = choice(t)
# print(computer)


while True:
    player = input("Rock? Paper? Scissors?")
    computer  = choice(t)
    if computer == player:
        print("Again :)")
    else:
        if computer == "Rock" and player == "Scissors":
            print("You lost... Computer won")
        else:
            print("You win")
            break
        if computer == 'Paper' and player == "Scissors":
            print("You lost ... Computer won")
        else:
            print("You win")
            break
        if computer == 'Scissors' and player == "Rock":
            print("You lost . Computer won")
        else:
            print("You win")
            break
        