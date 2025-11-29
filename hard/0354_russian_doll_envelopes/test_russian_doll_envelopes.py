import pytest
from russian_doll_envelopes import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    assert solution._max_envelopes(envelopes) == 3

def test_case_2(solution):
    envelopes = [[1,1],[1,1],[1,1]]
    assert solution._max_envelopes(envelopes) == 1

def test_case_3(solution):
    envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]
    assert solution._max_envelopes(envelopes) == 4

def test_case_4(solution):
    envelopes = []
    assert solution._max_envelopes(envelopes) == 0
