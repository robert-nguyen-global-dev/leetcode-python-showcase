import pytest
from course_schedule_ii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    numCourses = 2
    prerequisites = [[1, 0]]
    expected = [0, 1]
    assert solution._find_order(numCourses, prerequisites) == expected

def test_case_2(solution):
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = solution._find_order(numCourses, prerequisites)
    # Multiple valid answers: [0,1,2,3] or [0,2,1,3]
    assert result in [[0, 1, 2, 3], [0, 2, 1, 3]]

def test_case_3(solution):
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    assert solution._find_order(numCourses, prerequisites) == []

def test_case_4(solution):
    numCourses = 3
    prerequisites = []
    result = solution._find_order(numCourses, prerequisites)
    assert sorted(result) == [0, 1, 2]
