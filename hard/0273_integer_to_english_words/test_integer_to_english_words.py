import pytest
from integer_to_english_words import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._number_to_words(123) == "One Hundred Twenty Three"

def test_case_2(solution):
    assert solution._number_to_words(12345) == "Twelve Thousand Three Hundred Forty Five"

def test_case_3(solution):
    assert solution._number_to_words(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

def test_case_4(solution):
    assert solution._number_to_words(0) == "Zero"

def test_case_5(solution):
    assert solution._number_to_words(1000010) == "One Million Ten"
