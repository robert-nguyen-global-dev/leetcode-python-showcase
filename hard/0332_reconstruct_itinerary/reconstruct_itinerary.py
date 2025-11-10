from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Entry point for LeetCode submission.  
        Wrapper method to comply with LeetCode's required method name.

        Delegates to _find_itinerary() for actual implementation.
        """
        return self._find_itinerary(tickets)

    def _find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Internal implementation.  
        Uses DFS (Hierholzer’s Algorithm) to reconstruct the itinerary.

        Time Complexity: O(E log E) — sorting each adjacency list.  
        Space Complexity: O(E) — storing the graph and recursion stack.

        Args:
            tickets (List[List[str]]): List of flight tickets [from, to].

        Returns:
            List[str]: Reconstructed itinerary starting from 'JFK'.
        """
        # Step 1: Build graph with sorted destinations
        graph = defaultdict(list)
        for src, dst in sorted(tickets):
            graph[src].append(dst)

        route = []

        def dfs(airport: str):
            while graph[airport]:
                next_stop = graph[airport].pop(0)
                dfs(next_stop)
            route.append(airport)

        # Step 2: Start DFS from JFK
        dfs("JFK")

        # Step 3: Reverse route (Eulerian path built backwards)
        return route[::-1]
