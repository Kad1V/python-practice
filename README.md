# Python Practice

A collection of Python projects built while learning Python through hands-on practice.

## Projects

### 1. Guessing Game

A terminal game where you guess a randomly generated number from 1 to 100 in 7 attempts.

**Features**
- Random number generation
- Higher/lower hints
- Input validation
- Retry functionality

**Run**
```bash
python guessing_game.py
```

**Dependencies:** `readchar`

### 2. CLI To-Do App

A command-line task manager that allows you to manage tasks and persist them using JSON.

**Features**
- Add tasks
- List all tasks
- Mark tasks as completed
- Delete tasks
- Save and load tasks using JSON
- Input validation and error handling

**Run**
```bash
python todo.py
```

Tasks are stored in `to_do.json` in the working directory.

**Dependencies:** Python standard library.

**Testing**
```bash
python -m pytest -v
```

14 automated tests currently cover core functionality, edge cases, and JSON persistence.

## Setup

Clone the repository:

```bash
git clone https://github.com/Kad1V/python-practice.git
cd python-practice
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## What I'm Learning

- Python fundamentals
- Functions, lists, and dictionaries
- File handling and JSON
- Exception handling
- Virtual environments and dependencies
- Automated testing with pytest
- Git branching and pull requests

More projects and improvements will be added as I progress.