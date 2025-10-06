from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_order() for actual implementation.
        """
        return self._find_order(numCourses, prerequisites)

    def _find_order(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Internal implementation.  
        Using Topological Sort (Kahn's Algorithm).

        Time Complexity: O(V + E) — iterate through all nodes and edges once.  
        Space Complexity: O(V + E) — for adjacency list + indegree array.

        Args:
            numCourses (int): Total number of courses.
            prerequisites (List[List[int]]): Each pair [a, b] means course b must be taken before a.

        Returns:
            List[int]: A valid course order if possible, otherwise an empty list.
        """
        # Step 1: Build graph and indegree list
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 2: Initialize queue with all courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        # Step 3: BFS traversal
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 4: Check if all courses are processed
        return order if len(order) == numCourses else []
