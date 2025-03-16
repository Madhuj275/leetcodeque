# Problem: Divide Nodes Into the Maximum Number of Groups
# Difficulty: Unknown
# Solution:

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u):
            res = [u]
            visited[u] = True
            for v in graph[u]:
                if not visited[v]: 
                    res += dfs(v)
            return res
        
        def bfs(u):
            dist = {u: 1}
            q = deque([u])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in dist:
                        dist[v] = dist[u] + 1
                        q.append(v)
                    elif abs(dist[v] - dist[u]) != 1: 
                        return -1
            return max(dist.values())
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v); graph[v].append(u)
        
        visited = [False] * (n + 1)
        res = 0
        for u in range(1, n + 1):
            if not visited[u]:
                arr = dfs(u)
                count = max(bfs(v) for v in arr)
                if count == -1: 
                    return -1
                res += count
        return res