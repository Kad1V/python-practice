from guessing_game import check_guess
from guessing_game import get_guess


def test_invalid_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "hello")
    result = get_guess()
    assert result is None


def test_out_of_range(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 150)
    result = get_guess()
    assert result is None


def test_valid_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "50")
    result = get_guess()
    assert result == 50


def test_correct_guess():
    assert check_guess(50, 50) == "Win"


def test_too_low():
    assert check_guess(20, 50) == "Low"


def test_too_high():
    assert check_guess(60, 50) == "High"
