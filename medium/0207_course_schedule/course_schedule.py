from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _can_finish() for actual implementation.
        """
        return self._can_finish(numCourses, prerequisites)

    def _can_finish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Internal implementation.  
        Using Topological Sort (Kahn's Algorithm).

        Time Complexity: O(V + E) — iterate over all nodes and edges once.  
        Space Complexity: O(V + E) — graph adjacency list + indegree array.

        Args:
            numCourses (int): Total number of courses.
            prerequisites (List[List[int]]): Each pair [a, b] means course b must be taken before a.

        Returns:
            bool: True if all courses can be finished, False if there is a cycle.
        """
        # Step 1: Build graph and indegree list
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 2: Queue all courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        # Step 3: BFS traversal
        while queue:
            course = queue.popleft()
            visited += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 4: If visited all courses → True, else cycle exists → False
        return visited == numCourses
