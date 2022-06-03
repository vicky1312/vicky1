import random

while True:
    choices = ("R", "P" , "S")

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input ("R, P, or S?:")

    if player == CPU:
        print ("CPU:", CPU)
        print ("player:", player)
        print ("Tie!")

    elif player == "R":
        if CPU == "P":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("CPU wins")
        if CPU == "S":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("You win!")

    elif player == "P":
        if CPU == "R":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("You win!")
        if CPU == "S":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("CPU wins")

    elif player == "S":
        if CPU == "R":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("CPU wins")
        if CPU == "P":
            print ("CPU:", CPU)
            print ("player:", player)
            print ("You win!")

    play_again = input("Do you want to play again? y/n: ")
    if play_again != "y":
        break

print ("End.") 