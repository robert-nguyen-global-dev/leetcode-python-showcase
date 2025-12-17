import pytest
from maximum_xor_with_an_element_from_array import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [0,1,2,3,4]
    queries = [[3,1],[1,3],[5,6]]
    # Explanation:
    # query0: x=3, m=1 -> eligible nums = [0,1] -> best = 3 xor 0 = 3
    # query1: x=1, m=3 -> eligible nums = [0,1,2,3] -> best = 1 xor 2 = 3
    # query2: x=5, m=6 -> eligible nums = [0,1,2,3,4] -> best = 5 xor 2 = 7
    assert solution._maximize_xor(nums, queries) == [3, 3, 7]

def test_case_2(solution):
    nums = [5,2,4,6,6,3]
    queries = [[12,4],[8,1],[6,3]]
    # Expected: [-1, -1, 5]
    # query0: m=4 -> nums <=4: [2,3,4] -> best 12 xor 3 = 15 ? but 3<=4 yes -> however if none exist return -1 accordingly
    # We'll trust canonical expected from problem:
    assert solution._maximize_xor(nums, queries) == [15, -1, 5]

def test_case_3(solution):
    # Edge: no eligible nums for all queries
    nums = [10, 20, 30]
    queries = [[5, 1], [1, 0]]
    assert solution._maximize_xor(nums, queries) == [-1, -1]

def test_case_4(solution):
    # Single element nums
    nums = [7]
    queries = [[3,10], [3,6]]
    # for m=10 -> eligible [7] -> 3 xor 7 = 4 ; for m=6 -> no eligible -> -1
    assert solution._maximize_xor(nums, queries) == [4, -1]

def test_case_5(solution):
    # Larger random smoke test (deterministic)
    nums = [0,2,5,7,10]
    queries = [[6,5],[1,10],[15,7],[8,2]]
    # Expected results computed manually
    assert solution._maximize_xor(nums, queries) == [6, 11, 15, 10]
