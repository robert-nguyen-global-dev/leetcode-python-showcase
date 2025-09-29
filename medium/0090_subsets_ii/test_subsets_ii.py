import pytest
from subsets_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1,2,2]
    expected = [[], [1], [1,2], [1,2,2], [2], [2,2]]
    assert sorted(solution._subsets_with_dup(nums)) == sorted(expected)

def test_case_2(solution):
    nums = [0]
    expected = [[], [0]]
    assert sorted(solution._subsets_with_dup(nums)) == sorted(expected)

def test_case_3(solution):
    nums = [4,4,4,1,4]
    output = solution._subsets_with_dup(nums)
    # Kiểm tra không có subset nào bị trùng
    assert len(output) == len(set(tuple(x) for x in output))
