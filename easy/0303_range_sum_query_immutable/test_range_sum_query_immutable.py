import pytest
from range_sum_query_immutable import NumArray


@pytest.fixture
def num_array():
    return NumArray([-2, 0, 3, -5, 2, -1])


def test_case_1(num_array):
    assert num_array._sum_range(0, 2) == 1  # -2 + 0 + 3

def test_case_2(num_array):
    assert num_array._sum_range(2, 5) == -1  # 3 -5 +2 -1

def test_case_3(num_array):
    assert num_array._sum_range(0, 5) == -3

def test_single_element(num_array):
    assert num_array._sum_range(3, 3) == -5

def test_entire_array(num_array):
    assert num_array._sum_range(0, 5) == -3
