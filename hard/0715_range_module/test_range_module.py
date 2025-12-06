import pytest
from range_module import RangeModule


@pytest.fixture
def module():
    return RangeModule()


def test_case_1(module):
    module.addRange(10, 20)
    assert module.queryRange(10, 14) == True
    assert module.queryRange(13, 15) == True
    assert module.queryRange(20, 21) == False
    module.removeRange(14, 16)
    assert module.queryRange(13, 14) == True
    assert module.queryRange(14, 15) == False
    assert module.queryRange(16, 17) == True

def test_case_2(module):
    module.addRange(5, 8)
    module.addRange(1, 3)
    module.addRange(2, 6)
    assert module.queryRange(2, 5) == True
    module.removeRange(4, 7)
    assert module.queryRange(5, 6) == False
