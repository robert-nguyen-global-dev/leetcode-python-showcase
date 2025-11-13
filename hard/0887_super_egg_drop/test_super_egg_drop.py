import pytest
from super_egg_drop import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._super_egg_drop(1, 2) == 2  # 1 egg → must test sequentially

def test_case_2(solution):
    assert solution._super_egg_drop(2, 6) == 3  # Classic example

def test_case_3(solution):
    assert solution._super_egg_drop(3, 14) == 4

def test_case_4(solution):
    assert solution._super_egg_drop(4, 500) == 11
