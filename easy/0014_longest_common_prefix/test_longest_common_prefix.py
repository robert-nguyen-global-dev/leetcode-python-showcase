import pytest
from longest_common_prefix import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_case_1(solution):
    strs = ["flower", "flow", "flight"]
    assert solution._longest_common_prefix(strs) == "fl"

def test_example_case_2(solution):
    strs = ["dog", "racecar", "car"]
    assert solution._longest_common_prefix(strs) == ""

def test_identical_strings(solution):
    strs = ["python", "python", "python"]
    assert solution._longest_common_prefix(strs) == "python"

def test_single_string(solution):
    strs = ["leetcode"]
    assert solution._longest_common_prefix(strs) == "leetcode"

def test_empty_list(solution):
    strs = []
    assert solution._longest_common_prefix(strs) == ""

def test_empty_string_inside(solution):
    strs = ["", "hello", "hi"]
    assert solution._longest_common_prefix(strs) == ""
