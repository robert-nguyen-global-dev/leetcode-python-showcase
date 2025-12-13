import pytest
from count_all_valid_pickup_and_delivery_options import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    assert solution._count_orders(1) == 1

def test_case_2(solution):
    assert solution._count_orders(2) == 6

def test_case_3(solution):
    assert solution._count_orders(3) == 90

def test_case_4(solution):
    # Large input to ensure performance
    assert solution._count_orders(10) == 850728840
