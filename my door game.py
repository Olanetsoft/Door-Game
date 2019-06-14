import time
print("")
from random import *
print(time.asctime())
playing = True
attempt =0
score =0

print("""
Gameshow Are you ready ?

=========================
there is a puzzle behind one of the 3 door
Get the correct door to win the prize !!!

    _______      ________      _______
   |       |    |        |    |       |
   |       |    |        |    |       |
   |  [1]  |    |   [2]  |    |  [3]  |
   |       |    |        |    |       |
   |       |    |        |    |       |
    _______      ________      _______
""")


for attempt in range(3):
    print("\nChoose a door (1,2 or 3):")

    chosenDoor = input()
    chosenDoor = int(chosenDoor)

    winningDoor = randint(1,3)

    print("THE DOOR CHOSED IS",chosenDoor)
    print("THE WINNING DOOR IS",winningDoor)
    print("")
    attempt+=1
    if chosenDoor ==winningDoor:
        print("brilliant ! WELL DONE")
        print("attempt =",attempt)
    else:
        print("attempt =",attempt)
        print("unlucky! TRY AGAIN LATER")
        
print(" final attempt =",attempt)



#The user changes variable to end the game
from random import *
playing = True

score =0
print("""
Gameshow Are you ready ?

=========================
there is a puzzle behind one of the 3 door
Get the correct door to win the prize !!!

    _______      ________      _______
   |       |    |        |    |       |
   |       |    |        |    |       |
   |  [1]  |    |   [2]  |    |  [3]  |
   |       |    |        |    |       |
   |       |    |        |    |       |
    _______      ________      _______
""")


while playing == True:
    print("\nChoose a door (1,2 or 3):")

    chosenDoor = input()
    chosenDoor = int(chosenDoor)

    winningDoor = randint(1,3)

    print("THE DOOR CHOSED IS",chosenDoor)
    print("THE WINNING DOOR IS",winningDoor)
    print("")
    if chosenDoor ==winningDoor:
        print("brilliant ! WELL DONE")
        print("YOUR SCORE NOW IS",score)
        score+=5
    else:
        print("unlucky! TRY AGAIN ")
        print("YOUR SCORE NOW IS",score)
        score+=0
    

    print("\nDo you want to play again? (Y/N)")
    answer = input()

    if answer == "N":
        playing = False
print("THANKS FOR PLAYING")
print("YOUR FINAL SCORE IS: ",score)






        
