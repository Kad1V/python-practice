import random

secret = random.randint(1, 100)
guess = int(input("Enter your guess: "))
if guess == secret:
    print("Congratulations you win!!")
else:
    print("Sorry, try again next time.")
