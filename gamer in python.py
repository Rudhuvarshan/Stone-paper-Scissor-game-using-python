
import random
play=["stone","paper","scissor"]
computer=play[random.randint(0,2)]
player=False
while player==False:
        player=input("Rock,paper,scissor?")
        if player==computer:
            print("Tie")
        elif player=="stone":
            if computer== "paper":
                print("you lose",computer,"covers",player)
            else:
                print("you win",player,"smashes",computer)
        elif player=="paper":
            if computer=="scissor":
                print("you lose",computer,"covers",player)
            else:
                print("you won",player,"smashes",computer)
        elif player=="scissor":
            if computer=="rock":
                print("you lose",computer,"covers",player)
            else:
                print("you win",player,"smashes",computer)
        else:
            print("invalid operation")
        player=False
        computer=play[random.randint(0,2)]       
            
