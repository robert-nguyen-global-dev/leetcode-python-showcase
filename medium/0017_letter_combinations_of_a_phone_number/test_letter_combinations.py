import pytest
from letter_combinations import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case(solution):
    assert sorted(solution._letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    )

def test_single_digit(solution):
    assert sorted(solution._letter_combinations("2")) == sorted(["a", "b", "c"])

def test_digit_with_4_letters(solution):
    assert sorted(solution._letter_combinations("79")) == sorted([
        "pw","px","py","pz",
        "qw","qx","qy","qz",
        "rw","rx","ry","rz",
        "sw","sx","sy","sz"
    ])

def test_empty_input(solution):
    assert solution._letter_combinations("") == []

def test_long_input(solution):
    result = solution._letter_combinations("234")
    assert "adg" in result
    assert "cfi" in result
    assert len(result) == 27  # 3*3*3 combinations
