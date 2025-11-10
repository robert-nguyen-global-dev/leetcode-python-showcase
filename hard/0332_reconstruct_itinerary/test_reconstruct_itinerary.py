import pytest
from reconstruct_itinerary import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    assert solution._find_itinerary(tickets) == ["JFK","MUC","LHR","SFO","SJC"]

def test_case_2(solution):
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
               ["ATL","JFK"],["ATL","SFO"]]
    assert solution._find_itinerary(tickets) == ["JFK","ATL","JFK","SFO","ATL","SFO"]

def test_case_3(solution):
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    assert solution._find_itinerary(tickets) == ["JFK","NRT","JFK","KUL"]
