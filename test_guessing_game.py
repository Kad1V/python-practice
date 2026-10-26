from guessing_game import check_guess


def test_correct_guess():
    assert check_guess(50, 50) == "Win"


def test_too_low():
    assert check_guess(20, 50) == "Low"


def test_too_high():
    assert check_guess(60, 50) == "High"
