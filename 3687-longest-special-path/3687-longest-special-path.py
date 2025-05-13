class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        graph: list[dict[int, int]] = [{} for _ in range(len(nums))]
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        path: list[tuple[int, int]] = []  
        last_occurence: dict[int, int] = {}
        start: int = 0

        longest_length: int = -10**9
        minimum_number_of_nodes: int = 10**9

        def dfs(u: int, parent: int, distance_from_root: int) -> None:
            nonlocal start, longest_length, minimum_number_of_nodes

            old_nums_u_last_occurence: int = -1
            old_start: int = -1
            if nums[u] in last_occurence:
                old_nums_u_last_occurence = last_occurence[nums[u]]
                if last_occurence[nums[u]] >= start:
                    old_start = start
                    start = last_occurence[nums[u]] + 1
            path.append((u, distance_from_root))
            last_occurence[nums[u]] = len(path) - 1

            path_length: int = distance_from_root - path[start][1]
            num_nodes: int = len(path) - start

            if path_length > longest_length:
                longest_length = path_length
                minimum_number_of_nodes = num_nodes
            elif path_length == longest_length:
                minimum_number_of_nodes = min(minimum_number_of_nodes, num_nodes)

            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u, distance_from_root + graph[u][v])

            if old_start != -1:
                start = old_start

            if old_nums_u_last_occurence != -1:
                last_occurence[nums[u]] = old_nums_u_last_occurence
            else:
                del last_occurence[nums[u]]
            path.pop()


        dfs(0, -1, 0)

        return [longest_length, minimum_number_of_nodes]