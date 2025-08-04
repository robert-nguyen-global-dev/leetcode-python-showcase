import pytest
from first_bad_version import Solution

# Simulate external API
bad_version = None

def isBadVersion(version: int) -> bool:
    return version >= bad_version

@pytest.fixture
def solution(monkeypatch):
    monkeypatch.setattr("first_bad_version.isBadVersion", isBadVersion)
    return Solution()

def test_case_1(solution):
    global bad_version
    bad_version = 4
    assert solution._first_bad_version(5) == 4

def test_case_2(solution):
    global bad_version
    bad_version = 1
    assert solution._first_bad_version(1) == 1

def test_case_3(solution):
    global bad_version
    bad_version = 7
    assert solution._first_bad_version(10) == 7
