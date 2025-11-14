from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _min_camera_cover() for actual implementation.
        """
        return self._min_camera_cover(root)

    def _min_camera_cover(self, root: Optional[TreeNode]) -> int:
        """
        Internal implementation.  
        Uses post-order DFS to determine minimum number of cameras needed.

        States:
            0: Node needs a camera (not covered).
            1: Node has a camera.
            2: Node is covered by a child.

        Time Complexity: O(n) — visit every node exactly once.  
        Space Complexity: O(h) — recursion depth based on tree height.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: Minimum number of cameras required.
        """
        NEEDS_CAMERA = 0
        HAS_CAMERA = 1
        COVERED = 2

        self.camera_count = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return COVERED

            left_state = dfs(node.left)
            right_state = dfs(node.right)

            # If either child needs a camera, place camera here
            if left_state == NEEDS_CAMERA or right_state == NEEDS_CAMERA:
                self.camera_count += 1
                return HAS_CAMERA

            # If any child has a camera, this node is covered
            if left_state == HAS_CAMERA or right_state == HAS_CAMERA:
                return COVERED

            # Otherwise, this node needs a camera
            return NEEDS_CAMERA

        root_state = dfs(root)
        if root_state == NEEDS_CAMERA:
            self.camera_count += 1

        return self.camera_count
