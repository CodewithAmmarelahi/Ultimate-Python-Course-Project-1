import random

Choices = ["Rock", "Paper", "Scissors"]

User = input("Choose an option (Rock, Paper, Scissors): ").capitalize()

if User not in Choices:
    print("Invalid choice! Select Rock, Paper, or Scissors.")
else:
    System = random.choice(Choices)

    print(f"\nYou Chose: {User}")
    print(f"System Chose: {System}")

    if (System == "Rock" and User == "Scissors") or \
       (System == "Paper" and User == "Rock") or \
       (System == "Scissors" and User == "Paper"):
        print("You lose! System won!")

    elif (User == "Rock" and System == "Scissors") or \
         (User == "Paper" and System == "Rock") or \
         (User == "Scissors" and System == "Paper"):
        print("You Won!")

    else:
        print("It's a draw!")