# Provided by LeetCode:
class MountainArray:
    """
    Mock MountainArray class for local testing.
    """
    def __init__(self, arr):
        self.arr = arr
        self.calls = 0  # optional: đếm số lần gọi get()

    def get(self, index: int) -> int:
        self.calls += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_in_mountain_array() for actual implementation.
        """
        return self._find_in_mountain_array(target, mountain_arr)

    def _find_in_mountain_array(self, target: int, arr: 'MountainArray') -> int:
        """
        Internal implementation.  
        Using 3-phase Binary Search (Peak + Ascending + Descending).

        Time Complexity: O(log N)  
        Space Complexity: O(1)

        Args:
            target (int): target value to find
            arr (MountainArray): MountainArray interface

        Returns:
            int: index of target if found, else -1
        """
        # -----------------------
        # Step 1: Find peak index
        # -----------------------
        l, r = 0, arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if arr.get(mid) < arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # -----------------------
        # Step 2: Search ascending part [0..peak]
        # -----------------------
        idx = self._binary_search(arr, target, 0, peak, ascending=True)
        if idx != -1:
            return idx

        # -----------------------
        # Step 3: Search descending part [peak+1..n-1]
        # -----------------------
        return self._binary_search(arr, target, peak + 1, arr.length() - 1, ascending=False)

    def _binary_search(self, arr, target, l, r, ascending=True):
        """
        Generic binary search for ascending or descending segments.

        Time Complexity: O(log N)

        Args:
            arr (MountainArray): interface
            target (int): value to search
            l (int): left index
            r (int): right index
            ascending (bool): True if ascending, False if descending

        Returns:
            int: index if found else -1
        """
        while l <= r:
            mid = (l + r) // 2
            val = arr.get(mid)

            if val == target:
                return mid

            if ascending:
                if val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  # descending
                if val > target:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
