import random
while True:
    print("=" *35)
    print("WELCOME TO ROCK,PAPER,SCISSOR GAME")
    print("=" *35)
    print("choices u have:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Rules of the game:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")
    input("Press Enter to start the game...")
    user_choice = int(input("Enter your choice(1-3): "))
    import random
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    if user_choice == 1:
        user_choice = "Rock"
    elif user_choice == 2:
        user_choice = "Paper"
    elif user_choice == 3:
        user_choice = "Scissors"
    else:
        print("Invalid choice! Please choose a number between 1 and 3.")

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or(user_choice == "Scissors" and computer_choice == "Paper"):
        print(user_choice + " beats " + computer_choice)
        print("=" *13)
        print("You win!")
        print("=" *13)
    else:
        print(computer_choice + " beats " + user_choice)
        print("=" *15)
        print("Computer wins!")
        print("=" *15)
    play_again = input ("\nDo you want to play again? (y/n):").lower()

    if play_again != "y":
       print("Thanks for playing!")
       break
