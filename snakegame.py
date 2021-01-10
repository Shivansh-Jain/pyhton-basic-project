'''It is a similar game like stone, paper scissor , where the player plays with the computer , In this game player get's 5 chance in every round player have to make his choice between Snake ,Water, Scissor and computer will also choose between Snake ,Water ,Scissor. If player chooses snake and computer chooses water player will get one point(as snake will drink water) ,if player chooses water and computer chooses gun player will get one point(as gun gets drown in water).if player chooses gun and computer chooses snake player will get one point (as gun will kill the snake).
'''

import random

def game():
    name=input("Please enter your name: ")
    print(f"Welcome {name} let's play.")
    player = []
    computer = []
    tie = 0
    rounds = 5
    while rounds > 0:

        print(f"You have {rounds} numbers of round left.")
        a=input("Please pick your move (Snake=S,Water=W,Gun=G)+\n ").upper()
        if a not in ['S','W','G']:
            print("invalid input please pick (Snake=S,Water=W,Gun=G) ")
            rounds=rounds+1
        b=["snake","water","gun"]

        rounds=rounds-1
        comp=random.choice(b)

        if a=="S":
            if comp=="gun":
                computer.append("win")
            elif comp=="water":
                player.append("win")
            else:
                tie=tie+1
        elif a=="W":
            if comp=="snake":
                computer.append("win")
            elif comp=="gun":
                player.append("win")
            else:
                tie=tie+1
        elif a=="G":
            if comp=="snake":
                player.append("win")
            elif comp=="water":
                computer.append("win")
            else:
                tie=tie+1


    if len(player)>len(computer):
        print(f"Congratulation {name} you won the game.")
        print(f"Match score was {name}={len(player)} points, Computer={len(computer)} points, and tie={tie}")
    elif len(player)<len(computer):
        print(f"Sorry {name} you lost the game better luck next time.")
        print(f"Match score was {name}={len(player)} points, Computer={len(computer)} points, and tie={tie}")
    else:
        print("Match tied")
        print(f"Match score was {name}={len(player)} points, Computer={len(computer)} points.")


game()
