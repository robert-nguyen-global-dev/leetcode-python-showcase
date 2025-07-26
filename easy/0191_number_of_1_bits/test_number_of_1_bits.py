import pytest
from number_of_1_bits import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    assert solution._hamming_weight(11) == 3  # binary: 1011

def test_example_2(solution):
    assert solution._hamming_weight(128) == 1  # binary: 10000000

def test_example_3(solution):
    assert solution._hamming_weight(4294967293) == 31  # almost all bits are 1 (32-bit unsigned)

def test_zero(solution):
    assert solution._hamming_weight(0) == 0

def test_all_ones(solution):
    assert solution._hamming_weight(0xFFFFFFFF) == 32
