import random

while True:
    user = input("Choose rock, paper or scissors: ")

    computer = random.choice(["rock", "paper", "scissors"])

    print("Computer chose:", computer)

    if computer == user:
        print("Draw!")

    elif user == "rock" and computer == "scissors":
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You win!")

    elif user == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("Computer wins!")