import pytest
from guess_number_higher_or_lower import Solution

# ---- Mock guess API ----
# We'll use a global variable to simulate the picked number
SECRET_NUMBER = None

def guess(num: int) -> int:
    if num == SECRET_NUMBER:
        return 0
    elif num > SECRET_NUMBER:
        return -1
    else:
        return 1


@pytest.fixture
def solution(monkeypatch):
    # Monkeypatch the guess function in guess_number module
    import guess_number_higher_or_lower
    monkeypatch.setattr(guess_number_higher_or_lower, "guess", guess)
    return Solution()


def test_guess_number_exact(solution):
    global SECRET_NUMBER
    SECRET_NUMBER = 6
    assert solution._guess_number(10) == 6

def test_guess_number_first_number(solution):
    global SECRET_NUMBER
    SECRET_NUMBER = 1
    assert solution._guess_number(10) == 1

def test_guess_number_last_number(solution):
    global SECRET_NUMBER
    SECRET_NUMBER = 10
    assert solution._guess_number(10) == 10

def test_guess_number_middle(solution):
    global SECRET_NUMBER
    SECRET_NUMBER = 50
    assert solution._guess_number(100) == 50

def test_guess_number_not_exist(solution):
    global SECRET_NUMBER
    SECRET_NUMBER = 500
    assert solution._guess_number(100) == -1
