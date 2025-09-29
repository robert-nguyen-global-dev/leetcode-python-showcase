class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _subsets_with_dup() for actual implementation.
        """
        return self._subsets_with_dup(nums)

    def _subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        """
        Internal implementation.  
        Ensures no duplicate subsets are generated.

        Time Complexity: O(2^n) — all possible subsets.  
        Space Complexity: O(n) — recursion depth.

        Args:
            nums (list[int]): Input array possibly containing duplicates.

        Returns:
            list[list[int]]: Unique subsets.
        """
        res = []
        nums.sort()  # Quan trọng để xử lý duplicates

        def backtrack(start: int, path: list[int]):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicate
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
