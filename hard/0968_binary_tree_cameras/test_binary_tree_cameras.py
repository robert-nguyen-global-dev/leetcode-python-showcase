import pytest
from binary_tree_cameras import Solution, TreeNode


@pytest.fixture
def solution():
    return Solution()


def test_case_1(solution):
    # Tree: [0,0,null,0,0]
    root = TreeNode(0,
                    TreeNode(0,
                    TreeNode(0),
                    TreeNode(0)),
                    None)
    assert solution._min_camera_cover(root) == 1

def test_case_2(solution):
    # Tree: [0]
    root = TreeNode(0)
    assert solution._min_camera_cover(root) == 1

def test_case_3(solution):
    # Tree: [0,0,0,null,null,0,null,null,0]
    root = TreeNode(0,
                    TreeNode(0),
                    TreeNode(0,
                    TreeNode(0),
                    TreeNode(0)))
    assert solution._min_camera_cover(root) == 2
