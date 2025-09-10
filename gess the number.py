import random
# generate the number once
number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your guess (1-100),\n or 0 to exit: "))
    if guess == 0:
        print("Goodbye!")
        break

    attempts += 1
    if guess < number:
        print("Up ⬆️")
    elif guess > number:
        print("Down ⬇️")
    else:
        print(f"🎉 Correct! The number was {number}.\n You guessed it in {attempts} tries.")
        break
