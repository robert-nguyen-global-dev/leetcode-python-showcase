import pytest
from orderly_queue import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    s, k = "cba", 1
    assert solution._orderly_queue(s, k) == "acb"

def test_case_2(solution):
    s, k = "baaca", 3
    assert solution._orderly_queue(s, k) == "aaabc"

def test_case_3(solution):
    s, k = "aaa", 1
    assert solution._orderly_queue(s, k) == "aaa"
