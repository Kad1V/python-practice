import random

secret = random.randint(1, 100)

for i in range(1, 8):
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("Congratulations you win!!")
        break
    elif guess > secret:
        print("Lower!!")
        print(f"You have {7-i} tries left.")
    else:
        print("Higher!!")
        print(f"You have {7-i} tries left.")
