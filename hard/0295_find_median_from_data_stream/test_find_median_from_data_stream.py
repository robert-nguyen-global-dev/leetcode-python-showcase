import pytest
from find_median_from_data_stream import MedianFinder


def test_case_basic():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

def test_case_single_element():
    mf = MedianFinder()
    mf.addNum(5)
    assert mf.findMedian() == 5.0

def test_case_large_sequence():
    mf = MedianFinder()
    for num in [6, 10, 2, 8, 4]:
        mf.addNum(num)
    assert mf.findMedian() == 6.0

def test_case_even_count():
    mf = MedianFinder()
    for num in [1, 2, 3, 4]:
        mf.addNum(num)
    assert mf.findMedian() == 2.5
