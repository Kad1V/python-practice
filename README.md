# Guessing Game

It is a simple guessing game where you have to guess a number between 1 and 100. You only have 7 tries so use your guesses smartly.
Have Fun!!

## How to play
- The computer picks a number from 1 to 100.
- You have 7 tries. After each guess you get "Higher" or "Lower".
- Invalid input doesn't cost a try.
- Press r to play again.

## Setup
```bash
curl -O https://raw.githubusercontent.com/Kad1V/python-practice/main/guessing_game.py
python3 -m venv .venv
source .venv/bin/activate
pip install readchar
python guessing_game.py
```

## Run
```bash
python guessing_game.py
```

## What I practiced
- Loops, functions, input validation
- Virtual environments and dependencies
