import pytest
from course_schedule_iii import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    assert solution._schedule_course(courses) == 3

def test_case_2(solution):
    courses = [[1, 2]]
    assert solution._schedule_course(courses) == 1

def test_case_3(solution):
    courses = [[3, 2], [4, 3]]
    assert solution._schedule_course(courses) == 0

def test_case_4(solution):
    courses = [[5, 5], [4, 6], [2, 6]]
    assert solution._schedule_course(courses) == 2
