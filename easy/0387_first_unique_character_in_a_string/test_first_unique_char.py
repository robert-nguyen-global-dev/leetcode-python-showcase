import pytest
from first_unique_char import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    s = "leetcode"
    assert solution._first_unique_char(s) == 0

def test_case_2(solution):
    s = "loveleetcode"
    assert solution._first_unique_char(s) == 2

def test_case_3(solution):
    s = "aabb"
    assert solution._first_unique_char(s) == -1
