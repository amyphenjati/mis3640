import random


def number_guessing_game():
    """this function performs the guess the number game"""
    guess_taken = 0  # create variable to store number of guesses, starting from 0

    print("Hello! What is your name?")  # input name of player
    myName = input(">>")

    number = random.randint(1, 20)  # generate a random number between 1-20
    print(f"Well, {myName}, I am thinking of a number between 1 and 20.")

    while guess_taken < 6:  # if less than 6 guesses, repeat the following steps
        print("Take a guess.")
        guess = int(input(">>"))

        guess_taken = guess_taken + 1  # count number of guesses

        # output of guesses if not correct
        if guess < number:
            print("Your guess is too low.")

        elif guess > number:
            print("Your guess is too high.")

        # output if guess correctly
        else:
            print(
                f"Good job, {myName}! You guessed my number in {guess_taken} guesses!"
            )
            break

    if guess != number:  # if exceed 6 guesses
        print(f"Nope. The number I was thinking of was {number}")


def main():
    number_guessing_game()


if __name__ == "__main__":
    main()
