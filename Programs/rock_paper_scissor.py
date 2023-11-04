import random
computer = ["rock", "paper", "scissor"]
cpu = random.randint(0, 2)
player = input("Rock, paper or scissor?: ").upper()
print("Computer:", computer[cpu].upper())
print("Player:",player)
if (computer[cpu] == "rock" and player == "rock".upper()) or (computer[cpu] == "paper" and player == "paper".upper()) or (computer[cpu] == "scissor" and player == "scissor".upper()):
    print("Draw!")
elif (computer[cpu] == "rock" and player == "scissor".upper()) or (computer[cpu] == "paper" and player == "rock".upper()) or (computer[cpu] == "scissor" and player == "paper".upper()):
    print("Computer wins!")
elif (computer[cpu] == "scissor" and player == "rock".upper()) or (computer[cpu] == "rock" and player == "paper".upper()) or (computer[cpu] == "paper" and player == "scissor".upper()):
    print("Player wins!")
