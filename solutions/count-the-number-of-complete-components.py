# Problem: Count the Number of Complete Components
# Difficulty: Unknown
# Solution:

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        candidates = [frozenset([node] + graph[node]) for node in range(n)]
        return sum(len(component) == count for component, count in Counter(candidates).items())