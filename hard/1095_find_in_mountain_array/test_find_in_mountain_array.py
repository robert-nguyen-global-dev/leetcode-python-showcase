import pytest
from find_in_mountain_array import Solution, MountainArray

class TestMountainArray(MountainArray):
    """Mock class for offline testing."""
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    arr = TestMountainArray([1, 2, 3, 4, 5, 3, 1])
    assert solution._find_in_mountain_array(3, arr) == 2

def test_case_2(solution):
    arr = TestMountainArray([0, 1, 2, 4, 2, 1])
    assert solution._find_in_mountain_array(4, arr) == 3

def test_case_3(solution):
    arr = TestMountainArray([1, 5, 2])
    assert solution._find_in_mountain_array(2, arr) == 2

def test_target_not_found(solution):
    arr = TestMountainArray([1, 3, 5, 4, 2])
    assert solution._find_in_mountain_array(6, arr) == -1
