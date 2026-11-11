import random

rig=input("do you want to rig the game? (y/n): ")
if rig=="y" or rig=="Y" or rig=="yes" or rig=="Yes":
    heads=int(input("What percentage of odds do you want Heads to be? (1-100): "))
else: heads=50

choice = input("Welcome to coin flip game! Heads or Tails?: ").lower()

flip = random.randint(1, 100)
if flip <= heads:
    print("Heads")
else:
    print("Tails")



if flip <= heads and choice == "heads":
    print("You won!")
elif flip > heads and choice == "tails":
    print("You won!")
elif flip <= heads and choice == "tails":
    print("You lost!")
elif flip > heads and choice == "heads":
    print("You lost!")