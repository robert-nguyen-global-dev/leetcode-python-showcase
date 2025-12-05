import pytest
from maximum_sum_of_3_non_overlapping_subarrays import Solution


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    assert solution._max_sum_of_three_subarrays(nums, k) == [0, 3, 5]

def test_case_2(solution):
    nums = [1,2,1,2,1,2,1,2,1]
    k = 2
    # multiple equal totals -> expect lexicographically smallest
    assert solution._max_sum_of_three_subarrays(nums, k) == [0, 2, 4]

def test_case_3(solution):
    nums = [4,5,10,6,11,17,4,3,2,1,8,9]
    k = 3
    # check with larger windows
    result = solution._max_sum_of_three_subarrays(nums, k)
    # verify sums are maximal
    ws = []
    for idx in result:
        ws.append(sum(nums[idx:idx+k]))
    # compute brute-force maximum for verification
    best = -1
    best_combo = None
    n = len(nums)
    for i in range(0, n - 3*k + 1):
        for j in range(i + k, n - 2*k + 1):
            for l in range(j + k, n - k + 1):
                s = sum(nums[i:i+k]) + sum(nums[j:j+k]) + sum(nums[l:l+k])
                if s > best or (s == best and [i,j,l] < list(best_combo or [n,n,n])):
                    best = s
                    best_combo = [i,j,l]
    assert result == best_combo
