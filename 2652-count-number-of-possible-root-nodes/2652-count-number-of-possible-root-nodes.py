class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        guess_set = set((u, v) for u, v in guesses)
        
        initial_count = 0
        q = deque([(0, -1)])
        while q:
            u, parent = q.popleft()
            for v in adj[u]:
                if v != parent:
                    if (u, v) in guess_set:
                        initial_count += 1
                    q.append((v, u))
        
        ans = 1 if initial_count >= k else 0
        visited = [False] * n
        visited[0] = True
        q2 = deque([(0, initial_count)])
        
        while q2:
            u, cnt = q2.popleft()
            for v in adj[u]:
                if not visited[v]:
                    new_cnt = cnt
                    if (u, v) in guess_set:
                        new_cnt -= 1
                    if (v, u) in guess_set:
                        new_cnt += 1
                    if new_cnt >= k:
                        ans += 1
                    visited[v] = True
                    q2.append((v, new_cnt))
        return ans