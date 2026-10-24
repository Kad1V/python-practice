# Guessing Game

A terminal game where you guess a number from 1 to 100 in 7 tries

## How to play
- The computer picks a number from 1 to 100.
- You have 7 tries. After each guess you get "Higher" or "Lower".
- Invalid input doesn't cost a try.
- Press r to retry, any other key to quit.

## Setup
```bash
mkdir guessing-game && cd guessing-game
curl -O https://raw.githubusercontent.com/Kad1V/python-practice/main/guessing_game.py
python3 -m venv .venv
source .venv/bin/activate
pip install readchar
```

## Run
```bash
python guessing_game.py
```

## What I practiced
- Loops, functions, input validation
- Virtual environments and dependencies
