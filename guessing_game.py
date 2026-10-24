import random
import readchar


def check_guess(guess, secret, tries):
    if guess == secret:
        return True
    elif guess > secret:
        print("Lower!!")
        print(f"You have {7-tries} tries left.")
    else:
        print("Higher!!")
        print(f"You have {7-tries} tries left.")
    return False


while True:
    secret = random.randint(1, 100)
    tries = 0
    won = False

    while tries < 7:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Enter a Valid Guess.")
            continue
        if not 1 <= guess <= 100:
            print("!!Number must be between 1 and 100!!")
            continue
        tries += 1
        if check_guess(guess, secret, tries):
            won = True
            break

    if won:
        print("Congratulations you win!!")
        print(f"Your score is {7-tries+1}.")
    else:
        print("Oops, you lose.")
        print(f"The number was {secret}.")

    print("Press r to retry or press any other key to quit. ")
    retry = readchar.readkey().lower()
    if retry != "r":
        break
