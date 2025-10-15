import pytest
from path_sum_ii import Solution, TreeNode


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    # Tree: [5,4,8,11,None,13,4,7,2,None,None,5,1], target = 22
    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert sorted(solution._path_sum_dfs(root, 22)) == sorted(expected)

def test_case_2(solution):
    # Empty tree
    assert solution._path_sum_dfs(None, 0) == []

def test_case_3(solution):
    # Tree: [1,2,3], target = 5 → no valid path
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert solution._path_sum_dfs(root, 5) == []
