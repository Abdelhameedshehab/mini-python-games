import random

choices = ["paper", "rock", "scissors"]

player_score = 0
computer_score = 0

while True:
    # computer choice
    choice_1 = random.randint(1, 3)
    user_1 = choices[choice_1 - 1]

    # human choice
    choice_2 = int(input("Enter your choice:\n1. paper\n2. rock\n3. scissors\n0. Exit\n"))

    if choice_2 == 0:
        print("Goodbye!")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        break
    elif choice_2 not in [1, 2, 3]:
        print("Invalid choice!")
        continue

    user_2 = choices[choice_2 - 1]

    # show choices
    print("Computer chose: " + user_1)
    print("You chose: " + user_2)

    # game logic
    if user_1 == user_2:
        print("Draw")
    elif (user_1 == "paper" and user_2 == "scissors") or \
         (user_1 == "rock" and user_2 == "paper") or \
         (user_1 == "scissors" and user_2 == "rock"):
        print("You win")
        player_score += 1
    else:
        print("You lose")
        computer_score += 1

    # show score
    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")







