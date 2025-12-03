import pytest
from freedom_trail import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    ring = "godding"
    key = "gd"
    assert solution._find_rotate_steps(ring, key) == 4

def test_multiple_occurrences(solution):
    ring = "ababc"
    key = "bbc"
    assert solution._find_rotate_steps(ring, key) == 6

def test_single_char(solution):
    ring = "aaaaa"
    key = "aaa"
    # Only select moves (3), no rotation
    assert solution._find_rotate_steps(ring, key) == 3

def test_empty_key(solution):
    assert solution._find_rotate_steps("abc", "") == 0

def test_large_repetition(solution):
    ring = "xyzxyzxyz"
    key = "zzx"
    assert solution._find_rotate_steps(ring, key) > 0  # sanity check
