#ROCK PAPE AND SCISSORS GAME
#computer abd tess are playing thr above game
#Scores
tess_score = 0
computer_score = 0

#play upto five rounds and winner must have three out of 5 points:
#Importing the python library  
import random
choices = ["rock","paper","scissors"]

for round_number in range(1,6):
    print("round",round_number)
    
    #computer' choice
    computer_choice = random.choice(choices)
    print("Computer_chose:",computer_choice)

    #Tess' choice
    tess_choice = input("enter choice here")
    print("tess_choice")

    #Determine the winner
    if tess_choice == computer_choice:
        print("tie")
    elif (tess_choice == "scissors" and computer_choice == "paper")\
        or (tess_choice == "rock" and computer_choice == "scissors")\
        or (tess_choice == "paper" and computer_choice == "rock"):
        print("tess wins this round")
        tess_score += 1
    else:
        print("computer wins this round")
        computer_score += 1

    #show score
    print("score -tess:",tess_score,"score - computer:", computer_score)

    #end early if someone has 3 points
    if tess_score == 3 or computer_score == 3:
        break

#final result
print("GAME OVER!")
if tess_score > computer_score:
    print("tess wins!")
elif tess_score < computer_score:
    print("computer wins!")
else:
    print("its a tie!")
