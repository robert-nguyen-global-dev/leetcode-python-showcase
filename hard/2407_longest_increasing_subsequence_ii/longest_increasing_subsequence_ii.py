class Solution:
    def lengthOfLIS(self, nums, k):
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _length_of_lis() for actual implementation.
        """
        return self._length_of_lis(nums, k)

    def _length_of_lis(self, nums, k):
        """
        Internal implementation.  
        Uses coordinate compression + segment tree for range maximum queries.

        Time Complexity: O(n log n)  
        Space Complexity: O(n)

        Args:
            nums (List[int]): Input array of integers.
            k (int): Allowed max difference for LIS transitions.

        Returns:
            int: Length of the longest increasing subsequence under constraints.
        """
        # Step 1: Coordinate compression
        unique_values = sorted(set(nums))
        size = len(unique_values)

        def compress(value):
            # Binary search to find compressed index
            left, right = 0, size - 1
            while left <= right:
                mid = (left + right) // 2
                if unique_values[mid] == value:
                    return mid
                elif unique_values[mid] < value:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Segment tree arrays
        tree_size = 4 * size
        segment_tree = [0] * tree_size

        # Segment tree operations
        def update_tree(node, left, right, index, value):
            """Update segment tree at compressed index with dp value."""
            if left == right:
                segment_tree[node] = max(segment_tree[node], value)
                return

            mid = (left + right) // 2
            if index <= mid:
                update_tree(node * 2, left, mid, index, value)
            else:
                update_tree(node * 2 + 1, mid + 1, right, index, value)

            segment_tree[node] = max(segment_tree[node * 2], segment_tree[node * 2 + 1])

        def query_tree(node, left, right, query_left, query_right):
            """Range maximum query."""
            if query_right < left or right < query_left:
                return 0
            if query_left <= left and right <= query_right:
                return segment_tree[node]

            mid = (left + right) // 2
            left_result = query_tree(node * 2, left, mid, query_left, query_right)
            right_result = query_tree(node * 2 + 1, mid + 1, right, query_left, query_right)
            return max(left_result, right_result)

        longest_lis_length = 1

        # Step 2: Process elements in original order
        for value in nums:
            current_compressed = compress(value)

            # Determine valid range of previous values
            lower_value = value - k

            # Find left bound via binary search
            left, right = 0, size - 1
            while left <= right:
                mid = (left + right) // 2
                if unique_values[mid] < lower_value:
                    left = mid + 1
                else:
                    right = mid - 1
            left_bound = left

            # Query best dp in range
            best_previous = query_tree(1, 0, size - 1, left_bound, current_compressed)

            # dp[value] = best_previous + 1
            current_dp_value = best_previous + 1
            longest_lis_length = max(longest_lis_length, current_dp_value)

            # Update segment tree
            update_tree(1, 0, size - 1, current_compressed, current_dp_value)

        return longest_lis_length
