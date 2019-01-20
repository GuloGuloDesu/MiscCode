from random import choice
print("We are going to play rock, paper, scissors")
print("This will be the best of 3 rounds")

human_wins = 0
computer_wins = 0
winning_score = 3

while human_wins < winning_score and computer_wins < winning_score:
    print(f"\nHuman Score: {human_wins} Computer Score: {computer_wins}")
    print("Please choose rock, paper, or scissors")
    human = input().lower()
    if human == "quit" or human == "q":
        break
    print("Very crafty. Okay computer, rock, paper or scissors?")
    print("Shoot!")
    computer = choice(['rock', 'paper', 'scissors'])
    
    print(f"The human played: {human}\nThe computer played: {computer}")
    
    if human == computer:
        print("It's a tie")
    elif human == "rock":
        if computer == "scissors":
            print("Human wins\n")
            human_wins += 1
        else:
            print ("Computer wins\n")
            computer_wins += 1
    elif human == "paper":
        if computer == "scissors":
            print("Computer wins\n")
            computer_wins += 1
        else:
            print("Human wins\n")
            human_wins += 1
    elif human == "scissors":
        if computer == "paper":
            print("Human wins\n")
            human_wins += 1
        else:
            print("Computer wins\n")
            computer_wins += 1
    else:
        print("Your shit be broken son")
if human_wins == winning_score:
    print("Congrats, you beat the machine")
elif computer_wins == winning_score:
    print("Losers will be assimilated")
else:
    print("We all get a little scared sometimes [cough] *pussy* [/cough]")
print(f"Final Score\nHuman: {human_wins}\nComputer: {computer_wins}")
