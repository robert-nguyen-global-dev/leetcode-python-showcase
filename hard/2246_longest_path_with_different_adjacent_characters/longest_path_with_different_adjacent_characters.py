from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _longest_path() for actual implementation.
        """
        return self._longest_path(parent, s)

    def _longest_path(self, parent: List[int], s: str) -> int:
        """
        Internal implementation.  
        DFS on tree and compute longest path with different adjacent characters.

        Time Complexity: O(n) — processes each node once.  
        Space Complexity: O(n) — adjacency list + recursion stack.

        Args:
            parent (List[int]): Parent array describing the tree.
            s (str): String where s[i] is character of node i.

        Returns:
            int: Length of the longest valid path.
        """
        number_of_nodes = len(parent)

        # Step 1: Build adjacency list
        adjacency_list = [[] for _ in range(number_of_nodes)]
        for child_node in range(1, number_of_nodes):
            parent_node = parent[child_node]
            adjacency_list[parent_node].append(child_node)

        # Global max path
        longest_valid_path = 1

        # Step 2: DFS traversal
        def dfs(current_node):
            nonlocal longest_valid_path

            # Track the two longest valid chains from children
            longest_chain = 0
            second_longest_chain = 0

            for child_node in adjacency_list[current_node]:
                child_chain_length = dfs(child_node)

                # Skip if same character → cannot extend path
                if s[child_node] == s[current_node]:
                    continue

                # Update top-2 best chains
                if child_chain_length > longest_chain:
                    second_longest_chain = longest_chain
                    longest_chain = child_chain_length
                elif child_chain_length > second_longest_chain:
                    second_longest_chain = child_chain_length

            # Combine two children chains through current node
            current_best_path = longest_chain + second_longest_chain + 1
            longest_valid_path = max(longest_valid_path, current_best_path)

            # Return best downward chain
            return longest_chain + 1

        # Root is always node 0
        dfs(0)

        return longest_valid_path
