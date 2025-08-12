import pytest
from binary_watch import Solution


@pytest.fixture
def solution():
    return Solution()


def test_binary_watch_turned_on_1(solution):
    result = solution._read_binary_watch(1)
    # Just check a few expected values
    assert "0:01" in result
    assert "1:00" in result
    assert "0:32" in result

def test_binary_watch_turned_on_0(solution):
    assert solution._read_binary_watch(0) == ["0:00"]

def test_binary_watch_turned_on_max(solution):
    # If more LEDs than possible, expect empty list
    assert solution._read_binary_watch(10) == []
