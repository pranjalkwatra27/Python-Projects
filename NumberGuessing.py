import random

num = random.randint(1, 100)

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == 'easy':

    for i in range(1, 11):

        guess = int(input("Guess a number between 1 and 100: "))

        if guess == num:
            print("You guessed it in " + str(i) + " guesses")
            break

        elif guess > num:
            print("Too high")

        else:
            print("Too low")

        print("You have " + str(10 - i) +
              " attempts remaining to guess the number")

    else:
        print("You've run out of guesses.")
        print("The number was " + str(num))


if choice == 'hard':

    for i in range(1, 6):

        guess = int(input("Guess a number between 1 and 100: "))

        if guess == num:
            print("You guessed it in " + str(i) + " guesses")
            break

        elif guess > num:
            print("Too high")

        else:
            print("Too low")

        print("You have " + str(5 - i) +
              " attempts remaining to guess the number")

    else:
        print("You've run out of guesses.")
        print("The number was " + str(num))
