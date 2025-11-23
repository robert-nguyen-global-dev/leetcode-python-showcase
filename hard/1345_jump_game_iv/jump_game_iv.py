from collections import deque, defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _min_jumps() for actual implementation.
        """
        return self._min_jumps(arr)

    def _min_jumps(self, arr: List[int]) -> int:
        """
        Internal implementation.  
        BFS traversal where each index is a node and edges include:
        - i - 1
        - i + 1
        - all positions j where arr[j] == arr[i]

        Time Complexity: O(n).  
        Space Complexity: O(n)

        Args:
            arr (List[int]): Integer array representing the game.

        Returns:
            int: Minimum number of jumps to reach the last index.
        """
        array_length = len(arr)

        # Edge case: array of length 1 → already at the target
        if array_length == 1:
            return 0

        # Step 1: Build map arr value → list of indices
        value_to_indices = defaultdict(list)
        for index, value in enumerate(arr):
            value_to_indices[value].append(index)

        # Step 2: BFS setup
        bfs_queue = deque([0])
        visited = set([0])
        number_of_jumps = 0

        # Step 3: BFS loop
        while bfs_queue:
            queue_size = len(bfs_queue)

            for _ in range(queue_size):
                current_index = bfs_queue.popleft()

                # If we reach the last index → done
                if current_index == array_length - 1:
                    return number_of_jumps

                current_value = arr[current_index]

                # Explore neighbors: i - 1, i + 1, and teleport to same-value indices
                neighbors = []

                # i - 1
                if current_index - 1 >= 0:
                    neighbors.append(current_index - 1)

                # i + 1
                if current_index + 1 < array_length:
                    neighbors.append(current_index + 1)

                # All indices with same value → teleport jump
                neighbors.extend(value_to_indices[current_value])

                # Process neighbors
                for neighbor_index in neighbors:
                    if neighbor_index not in visited:
                        visited.add(neighbor_index)
                        bfs_queue.append(neighbor_index)

                # Clear the list to avoid future redundant processing
                value_to_indices[current_value].clear()

            number_of_jumps += 1

        return number_of_jumps
