from random import randint

#create a list of play option variable list
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer player
computer = t[randint(0,2)]

#set player to false
player = False

for t in range (10,38):

    while player == False:
        player = input("Rock, Paper, Scissors?")
        player = player.strip()
        player = player.capitalize()
        if player == computer:
            print("tie")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose")
            else:
                print("You win!")
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose")
            else:
                print("You win!")
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose")
            else:
                print("You win!")
        else:
            print("Invalid entry")
    player = False
computer = t[radint(0,2)]


