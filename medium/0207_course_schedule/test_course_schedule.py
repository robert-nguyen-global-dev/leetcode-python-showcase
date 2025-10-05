import pytest
from course_schedule import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    numCourses = 2
    prerequisites = [[1, 0]]
    assert solution._can_finish(numCourses, prerequisites) == True

def test_case_2(solution):
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert solution._can_finish(numCourses, prerequisites) == False

def test_case_3(solution):
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    assert solution._can_finish(numCourses, prerequisites) == True

def test_case_4(solution):
    numCourses = 3
    prerequisites = [[1, 0], [2, 1], [0, 2]]
    assert solution._can_finish(numCourses, prerequisites) == False
