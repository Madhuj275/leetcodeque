class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        gt = set((i, j) for i, j in guesses)
        @cache
        def get_correct_pairs(i, parent):
            next_nodes = graph[i]
            n_correct = 0
            for next_node in next_nodes:
                if next_node == parent:
                    continue
                if (i, next_node) in gt:
                    n_correct += 1
                n_correct += get_correct_pairs(next_node, i)
            return n_correct
        
        ans = 0
        for i in graph:
            if get_correct_pairs(i, None) >= k:
                ans += 1
        return ans
            