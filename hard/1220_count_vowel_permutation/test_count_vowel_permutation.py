import pytest
from count_vowel_permutation import Solution


@pytest.fixture
def solution():
    return Solution()


def test_n_1(solution):
    # n = 1 -> each vowel alone: 5
    assert solution._count_vowel_permutation(1) == 5

def test_n_2(solution):
    # n = 2 -> known result: 10
    assert solution._count_vowel_permutation(2) == 10

def test_n_5(solution):
    # Example from problem statements / common references: n = 5 -> 68
    assert solution._count_vowel_permutation(5) == 68

def test_zero_or_negative(solution):
    # edge cases: n <= 0 -> 0 permutations by our definition
    assert solution._count_vowel_permutation(0) == 0
    assert solution._count_vowel_permutation(-3) == 0
